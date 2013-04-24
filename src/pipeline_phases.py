# coding: utf-8

from instructions import *
from bitstring import BitArray


def get_register_position(code, start, end):

    if start == 0 and end != 31:
        b = BitArray(bin=code[-end:])
        return b.uint
    elif start != 0 and end != 31:
        b = BitArray(bin=code[-end:-start])
        return b.uint
    elif start != 0 and end == 31:
        b = BitArray(bin=code[:-start])
        return b.uint
    elif start == 0 and end == 31:
        b = BitArray(bin=code[:])
        return b.uint


class PipelinePhase(object):

    def __init__(self):
        self.current_instruction = NOP()

    def action(self):
        raise NotImplementedError('Method from an abstract class')

    def try_to_return_instruction(self):
        instruction_to_pass = self.current_instruction
        self.current_instruction = NOP()
        return instruction_to_pass


class PipelinePhaseIF(PipelinePhase):

    def __init__(self):
        super(PipelinePhaseIF, self).__init__()

    def instantiate_instruction(self, code):
            opcode = code[0:6]
            if opcode == '000000':
                funct = code[-6:]
                #NOP
                if funct == '000000':
                    return NOP()
                #ADD
                elif funct == '100000':
                    return ADD(code)
                #SUB
                elif funct == '100010':
                    return SUB(code)
                #MUL
                elif funct == '011000':
                    return MUL(code)

            #Addi
            elif opcode == '001000':
                return ADDi(code)
            #Lw
            elif opcode == '100011':
                return LW(code)
            #Sw
            elif opcode == '101011':
                return SW(code)
            #BEQ
            elif opcode == '000101':
                return BEQ(code)
            #BLE
            elif opcode == '000111':
                return BLE(code)
            #BNE
            elif opcode == '000100':
                return BNE(code)
            #Jmp
            elif opcode == '000010':
                return JMP(code)

            else:
                raise ValueError("opcode value not valid")

    #checks if the instruction will load a register that is scheduled to be written
    def has_RAW_dependency(self, next_instruction, registers):
        next_instruction_code = next_instruction.code

        if isinstance(next_instruction, NOP) or isinstance(next_instruction, JMP):
            return False

        elif (isinstance(next_instruction, ADD) or isinstance(next_instruction, SUB) or
                isinstance(next_instruction, MUL) or isinstance(next_instruction, BEQ) or
                isinstance(next_instruction, BLE) or isinstance(next_instruction, BNE) or
                isinstance(next_instruction, SW)):
            return (registers[get_register_position(next_instruction_code, 16, 21)].is_waiting_for_use() or
                    registers[get_register_position(next_instruction_code, 21, 26)].is_waiting_for_use())

        elif isinstance(next_instruction, ADDi) or isinstance(next_instruction, LW) or isinstance(next_instruction, SW):
            return registers[get_register_position(next_instruction_code, 21, 26)].is_waiting_for_use()
        else:
            raise ValueError("instruction not valid")

    def has_PC_READ_dependency(self, PC_counter):
        return PC_counter.is_waiting_for_use()

    def set_next_write_use(self, instruction, registers, PC_counter):
        opcode = instruction.code[0:6]
        if opcode == '000000':
            funct = instruction.code[-6:]
            #NOP
            if funct == '000000':
                return
            #ADD, SUB and MUL
            else:
                registers[instruction.get_register_position(11, 16)].declare_last_write_use(instruction)
                return

        #Addi, Lw
        elif opcode == '001000' or opcode == '100011':
            registers[instruction.get_register_position(16, 21)].declare_last_write_use(instruction)
            return
        #Sw
        elif opcode == '101011':
            #check what we should do regarding memory RAW dependency
            return
        #Beq,Ble, Bne, Jmp
        elif opcode == '000101' or opcode == '000111' or opcode == '000100' or opcode == '000010':
            return PC_counter.declare_last_write_use(instruction)
            return
        else:
            raise ValueError("opcode value not valid")

    def action(self, PC_array, PC_counter, registers):
        #ver se é pra carregar uma nova instrução ou deixar a q tá (caso do MUL)
        #pegar a instrução, ver qual registradores usa, ver se pode carregar ou se é NOP
        #ver se o pc tá sendo usado pra write
        #se for pra carregar, carrega, e se for de write, seta o next_write_use
        #mexer no pc
        if isinstance(self.current_instruction, NOP):
            #if we do not have more instructions, we always load NOP() (which is already loaded)
            if PC_counter.get_value()/4 >= len(PC_array):
                return
            next_instruction_code = PC_array[PC_counter.get_value()/4]
            next_instruction = self.instantiate_instruction(next_instruction_code)
            if (not self.has_RAW_dependency(next_instruction, registers)) and (not self.has_PC_READ_dependency(PC_counter)):
                self.current_instruction = next_instruction
                PC_counter.write(PC_counter.get_value()+4, self)
                self.set_next_write_use(self.current_instruction, registers, PC_counter)
            else:
                self.current_instruction = NOP()


class PipelinePhaseID(PipelinePhase):

    def __init__(self):
        super(PipelinePhaseID, self).__init__()

    def action(self, if_phase, registers):
        if isinstance(self.current_instruction, NOP):
            self.current_instruction = if_phase.try_to_return_instruction()
            self.current_instruction.action_ID(registers)


class PipelinePhaseEX(PipelinePhase):

    def __init__(self):
        super(PipelinePhaseEX, self).__init__()

    def action(self, id_phase):
        if isinstance(self.current_instruction, NOP):
            self.current_instruction = id_phase.try_to_return_instruction()
        self.current_instruction.action_EX()

    def try_to_return_instruction(self):
        if self.current_instruction.is_finished():
            return PipelinePhase.try_to_return_instruction(self)
        else:
            return NOP()


class PipelinePhaseMEM(PipelinePhase):

    def __init__(self):
        super(PipelinePhaseMEM, self).__init__()

    def action(self, ex_phase, mem, PC_counter, recent_mem):
        self.current_instruction = ex_phase.try_to_return_instruction()
        self.current_instruction.action_MEM(mem, PC_counter, recent_mem)


class PipelinePhaseWB(PipelinePhase):

    def __init__(self):
        super(PipelinePhaseWB, self).__init__()

    def action(self, mem_phase, registers, fin_instr):
        self.current_instruction = mem_phase.try_to_return_instruction()
        if not isinstance(self.current_instruction, NOP):
            fin_instr[0] += 1
        self.current_instruction.action_WB(registers)


class PipelinePhaseIF_Bypassing(PipelinePhaseIF):

    def __init__(self):
        super(PipelinePhaseIF, self).__init__()

    def has_RAW_dependency(self, next_instruction, registers):
        if isinstance(next_instruction, LW):
            pass
            # return registers[get_register_position(next_instruction_code, 21, 26)].is_waiting_for_use()
        return False

# coding: utf-8
from bitstring import BitArray


class Instruction():

    def is_finished(self):
        return True

    def get_register_position(self, start, end):

        if start == 0 and end != 31:
            b = BitArray(bin=self.code[-end:])
            return b.uint
        elif start != 0 and end != 31:
            b = BitArray(bin=self.code[-end:-start])
            return b.uint
        elif start != 0 and end == 31:
            b = BitArray(bin=self.code[:-start])
            return b.uint
        elif start == 0 and end == 31:
            b = BitArray(bin=self.code[:])
            return b.uint

    def get_immediate_value(self):

        b = BitArray(bin=self.code[-16:])
        return int(b.int)

    def action_ID(self, registers):
        raise NotImplementedError('This is an abstract class.')

    def action_EX(self):
        raise NotImplementedError('This is an abstract class.')

    def action_MEM(self, mem, PC_counter, recent_mem):
        raise NotImplementedError('This is an abstract class.')

    def action_WB(self, registers):
        raise NotImplementedError('This is an abstract class.')

    def get_control_signals(self):
        raise NotImplementedError('This is an abstract class.')


class NOP(Instruction):
    def action_ID(self, registers):
        pass

    def action_EX(self):
        pass

    def action_MEM(self, mem, PC_counter, recent_mem):
        pass

    def action_WB(self, registers):
        pass

    def __str__(self):
        return "NOP"

    def get_control_signals(self):
        return {}


# Instrucao vai ser Rd = Rs + Rt
class ADD(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code

    
    def get_computed_value(self):
        return self.Rd  

    def action_ID(self, registers):

        if hasattr(self, 'Rs_instruction'):
            self.Rs = self.Rs_instruction.get_computed_value()
        else:
             # 26 to 21
            self.Rs = registers[self.get_register_position(21, 26)].get_value()
        

        if hasattr(self, 'Rt_instruction'):
            self.Rt = self.Rt_instruction.get_computed_value()
        else:    
            # 21 to 16
            self.Rt = registers[self.get_register_position(16, 21)].get_value()

    def action_EX(self):
        self.Rd = self.Rs + self.Rt

    def action_MEM(self, mem, PC_counter, recent_mem):
        pass

    def action_WB(self, registers):
        # Rd: 16 to 11
        registers[self.get_register_position(11, 16)].write(self.Rd, self)

    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor
    def get_control_signals(self):
        control_signals = {"RegDst": 1,
                           "ALUSrc": 0,
                           "MemtoReg": 0,
                           "RegWrite": 1,
                           "MemWrite": 0,
                           "Branch": 0,
                           "Jump": 0,
                           "ALUOp1": 1,
                           "ALUOp2": 0,
                           "MemRead": 0,
                           "ExtOp": 'x'}
        return control_signals

    def __str__(self):
        return "ADD R"+str(self.get_register_position(11, 16))+", R"+str(self.get_register_position(21, 26))+", R"+str(self.get_register_position(16, 21))


class ADDi(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code

    def get_computed_value(self):
        return self.Rt  


    def action_ID(self, registers):
        
        if hasattr(self, 'Rs_instruction'):
            self.Rs = self.Rs_instruction.get_computed_value()
        else:
             # 26 to 21
            self.Rs = registers[self.get_register_position(21, 26)].get_value()

        # 16 to 0
        self.ImmExt = self.get_immediate_value()

    def action_EX(self):
        self.Rt = self.Rs + self.ImmExt

    def action_MEM(self, mem, PC_counter, recent_mem):
        pass

    def action_WB(self, registers):
        # Rt: 16 to 21
        registers[self.get_register_position(16, 21)].write(self.Rt, self)

    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor

    # valores INCORRETOS! Falta confirmar se os valores do ADD são os mesmos do Addi
    def get_control_signals(self):
        control_signals = {"RegDst": 1,
                           "ALUSrc": 0,
                           "MemtoReg": 0,
                           "RegWrite": 1,
                           "MemWrite": 0,
                           "Branch": 0,
                           "Jump": 0,
                           "ALUOp1": 1,
                           "ALUOp2": 0,
                           "MemRead": 0,
                           "ExtOp": 'x'}
        return control_signals

    def __str__(self):
        return "ADDi R"+str(self.get_register_position(16, 21))+", R"+str(self.get_register_position(21, 26))+", "+str(self.get_immediate_value())


# Instrucao vai ser Rd = Rs - Rt
class SUB(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code

    def get_computed_value(self):
        return self.Rd  

    def action_ID(self, registers):
        if hasattr(self, 'Rs_instruction'):
            self.Rs = self.Rs_instruction.get_computed_value()
        else:
             # 26 to 21
            self.Rs = registers[self.get_register_position(21, 26)].get_value()
        

        if hasattr(self, 'Rt_instruction'):
            self.Rt = self.Rt_instruction.get_computed_value()
        else:    
            # 21 to 16
            self.Rt = registers[self.get_register_position(16, 21)].get_value()

    def action_EX(self):
        self.Rd = self.Rs - self.Rt

    def action_MEM(self, mem, PC_counter, recent_mem):
        pass

    def action_WB(self, registers):
        # Rd: 16 to 11
        registers[self.get_register_position(11, 16)].write(self.Rd, self)

    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor
    def get_control_signals(self):
        control_signals = {"RegDst": 0,
                           "ALUSrc": 0,
                           "MemtoReg": 0,
                           "RegWrite": 1,
                           "MemWrite": 0,
                           "Branch": 0,
                           "Jump": 0,
                           "ALUOp1": 1,
                           "ALUOp2": 0,
                           "MemRead": 0,
                           "ExtOp": "x"}
        return control_signals

    def __str__(self):
        return "SUB R"+str(self.get_register_position(11, 16))+", R"+str(self.get_register_position(21, 26))+", R"+str(self.get_register_position(16, 21))


# Instrucao vai ser Rd = Rs*Rt
class MUL(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code
        self.execution_state = 2

    def get_computed_value(self):
        return self.Rd  

    def action_ID(self, registers):
        if hasattr(self, 'Rs_instruction'):
            self.Rs = self.Rs_instruction.get_computed_value()
        else:
             # 26 to 21
            self.Rs = registers[self.get_register_position(21, 26)].get_value()
        

        if hasattr(self, 'Rt_instruction'):
            self.Rt = self.Rt_instruction.get_computed_value()
        else:    
            # 21 to 16
            self.Rt = registers[self.get_register_position(16, 21)].get_value()

    def action_EX(self):
        self.Rd = self.Rs * self.Rt
        self.execution_state -= 1

    def action_MEM(self, mem, PC_counter, recent_mem):
        pass

    def action_WB(self, registers):
        # Rd: 16 to 11
        registers[self.get_register_position(11, 16)].write(self.Rd, self)

    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor

    def get_control_signals(self):
        control_signals = {"RegDst": 1,
                           "ALUSrc": 0,
                           "MemtoReg": 0,
                           "RegWrite": 1,
                           "MemWrite": 0,
                           "Branch": 0,
                           "Jump": 0,
                           "ALUOp1": 1,
                           "ALUOp2": 0,
                           "MemRead": 0,
                           "ExtOp": "x"}
        return control_signals

    def is_finished(self):
        return self.execution_state == 0

    def __str__(self):
        return "MUL R"+str(self.get_register_position(11, 16))+", R"+str(self.get_register_position(21, 26))+", R"+str(self.get_register_position(16, 21))


# Instrucao vai ser if(Rs==Rt) => pc+=4+Imm
class BEQ(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code


    def action_ID(self, registers):
        
        if hasattr(self, 'Rs_instruction'):
            self.Rs = self.Rs_instruction.get_computed_value()
        else:
             # 26 to 21
            self.Rs = registers[self.get_register_position(21, 26)].get_value()
        

        if hasattr(self, 'Rt_instruction'):
            self.Rt = self.Rt_instruction.get_computed_value()
        else:    
            # 21 to 16
            self.Rt = registers[self.get_register_position(16, 21)].get_value()


        # 16 to 0
        self.Imm = self.get_register_position(0, 16)

    def action_EX(self):
        pass

    def action_MEM(self, mem, PC_counter, recent_mem):
        print (self.Rs)
        print (self.Rt)
        if self.Rs == self.Rt:
            PC_counter.write((PC_counter.get_value()+self.Imm), self)
        else:
            PC_counter.concede_right_to_use(self)

    def action_WB(self, registers):
        pass

    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor

    def get_control_signals(self):
        control_signals = {"RegDst": "x",
                           "ALUSrc": 0,
                           "MemtoReg": "x",
                           "RegWrite": 0,
                           "MemWrite": 0,
                           "Branch": 1,
                           "Jump": 0,
                           "ALUOp1": 0,
                           "ALUOp2": 1,
                           "MemRead": 0,
                           "ExtOp": 'x'}
        return control_signals

    def __str__(self):
        return "BEQ R"+str(self.get_register_position(21, 26))+", R"+str(self.get_register_position(16, 21))+", "+str(self.get_register_position(0, 16))


# Instrucao vai ser if(Rs<=Rt) => pc=Imm
class BLE(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code

    def action_ID(self, registers):
        if hasattr(self, 'Rs_instruction'):
            self.Rs = self.Rs_instruction.get_computed_value()
        else:
             # 26 to 21
            self.Rs = registers[self.get_register_position(21, 26)].get_value()
        

        if hasattr(self, 'Rt_instruction'):
            self.Rt = self.Rt_instruction.get_computed_value()
        else:    
            # 21 to 16
            self.Rt = registers[self.get_register_position(16, 21)].get_value()

        # 16 to 0
        self.Imm = self.get_register_position(0, 16)

    def action_EX(self):
        pass

        
    def action_MEM(self, mem, PC_counter, recent_mem):
        if self.Rs <= self.Rt:
           PC_counter.write((self.Imm),self)
        else:
            PC_counter.concede_right_to_use(self)   

    def action_WB(self, registers):
        pass

    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor

    def get_control_signals(self):
        control_signals = {"RegDst": "x",
                           "ALUSrc": 0,
                           "MemtoReg": "x",
                           "RegWrite": 0,
                           "MemWrite": 0,
                           "Branch": 1,
                           "Jump": 0,
                           "ALUOp1": 0,
                           "ALUOp2": 1,
                           "MemRead": 0,
                           "ExtOp": 'x'}
        return control_signals

    def __str__(self):
        return "BLE R"+str(self.get_register_position(21, 26))+", R"+str(self.get_register_position(16, 21))+", "+str(self.get_register_position(0, 16))


# Instrucao vai ser if(Rs!=Rt) => pc+=4+Imm
class BNE(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code

    def action_ID(self, registers):
        if hasattr(self, 'Rs_instruction'):
            self.Rs = self.Rs_instruction.get_computed_value()
        else:
             # 26 to 21
            self.Rs = registers[self.get_register_position(21, 26)].get_value()

        if hasattr(self, 'Rt_instruction'):
            self.Rt = self.Rt_instruction.get_computed_value()
        else:
            # 21 to 16
            self.Rt = registers[self.get_register_position(16, 21)].get_value()

        # 16 to 0
        self.Imm = self.get_register_position(0, 16)

    def action_EX(self):
        pass

    def action_MEM(self, mem, PC_counter, recent_mem):
        if self.Rs != self.Rt:
            PC_counter.write((PC_counter.get_value()+self.Imm), self)
        else:
            PC_counter.concede_right_to_use(self)

    def action_WB(self, registers):
        pass

    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor

    def get_control_signals(self):
        control_signals = {"RegDst": "x",
                           "ALUSrc": 0,
                           "MemtoReg": "x",
                           "RegWrite": 0,
                           "MemWrite": 0,
                           "Branch": 1,
                           "Jump": 0,
                           "ALUOp1": 0,
                           "ALUOp2": 1,
                           "MemRead": 0,
                           "ExtOp": 'x'}
        return control_signals

    def __str__(self):
        return "BNE R"+str(self.get_register_position(21, 26))+", R"+str(self.get_register_position(16, 21))+", "+str(self.get_register_position(0, 16))


class JMP(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code

    def action_ID(self, registers):
        # 26 to 0
        self.PC = self.get_register_position(0, 26)

    def action_EX(self):
        pass

    def action_MEM(self, mem, PC_counter, recent_mem):
        PC_counter.write(self.PC, self)

    def action_WB(self, registers):
        pass

    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor

    def get_control_signals(self):
        control_signals = {"RegDst": "x",
                           "ALUSrc": "x",
                           "MemtoReg": "x",
                           "RegWrite": 0,
                           "MemWrite": 0,
                           "Branch": 0,
                           "Jump": 1,
                           "ALUOp1": 0,
                           "ALUOp2": 1,
                           "MemRead": 0,
                           "ExtOp": "x"}
        return control_signals

    def __str__(self):
        return "JMP "+str(self.get_register_position(0, 26))


class LW(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code

        self.phase_ID = False

    def get_computed_value(self):
        return self.Rt  

    def action_ID(self, registers):
        self.phase_ID = True
        if hasattr(self, 'Rs_instruction'):
            self.Rs = self.Rs_instruction.get_computed_value()
        else:
             # 26 to 21
            self.Rs = registers[self.get_register_position(21, 26)].get_value()
        
        # 16 to 0
        self.ImmExt = self.get_immediate_value()

    def action_EX(self):
        self.phase_ID = False

    def action_MEM(self, mem, PC_counter, recent_mem):
        address = self.Rs + self.ImmExt
        self.Rt = mem[(address - 1000)/4]
        recent_mem.pop()
        recent_mem.insert(0, (address, self.Rt))

    def action_WB(self, registers):
        # Rd: 16 to 11
        registers[self.get_register_position(16, 21)].write(self.Rt, self)

    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor

    def get_control_signals(self):
        control_signals = {"RegDst": 0,
                           "ALUSrc": 1,
                           "MemtoReg": 1,
                           "RegWrite": 1,
                           "MemWrite": 0,
                           "Branch": 0,
                           "Jump": 0,
                           "ALUOp1": 0,
                           "ALUOp2": 0,
                           "MemRead": 1,
                           "ExtOp": 1}
        return control_signals

    def __str__(self):
        return "LW R"+str(self.get_register_position(16, 21))+", "+str(self.get_immediate_value())+"("+str(self.get_register_position(21, 26))+")"


class SW(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code

    def get_computed_value(self):
        return self.Rt  

    def action_ID(self, registers):
        if hasattr(self, 'Rs_instruction'):
            self.Rs = self.Rs_instruction.get_computed_value()
        else:
             # 26 to 21
            self.Rs = registers[self.get_register_position(21, 26)].get_value()
        

        if hasattr(self, 'Rt_instruction'):
            self.Rt = self.Rt_instruction.get_computed_value()
        else:    
            # 21 to 16
            self.Rt = registers[self.get_register_position(16, 21)].get_value()

        # 16 to 0
        self.ImmExt = self.get_immediate_value()

    def action_EX(self):
        pass

    def action_MEM(self, mem, PC_counter, recent_mem):
        address = self.Rs + self.ImmExt
        mem[(address - 1000)/4] = self.Rt
        recent_mem.pop()
        recent_mem.insert(0, (address, self.Rt))

    def action_WB(self, registers):
        pass

    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor
    def get_control_signals(self):
        control_signals = {"RegDst": "x",
                           "ALUSrc": 1,
                           "MemtoReg": "x",
                           "RegWrite": 0,
                           "MemWrite": 1,
                           "Branch": 0,
                           "Jump": 0,
                           "ALUOp1": 0,
                           "ALUOp2": 0,
                           "MemRead": 0,
                           "ExtOp": 1}
        return control_signals

    def __str__(self):
        return "SW R"+str(self.get_register_position(16, 21))+", "+str(self.get_immediate_value())+"("+str(self.get_register_position(21, 26))+")"

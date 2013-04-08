# coding: utf-8

from instructions import NOP


class PipelinePhase(object):
    def __init__(self):
        self.current_instruction = NOP()
        
    def action(self):
        raise NotImplementedError('Method from an abstract class')
    
    def try_to_return_instruction(self):
        if isinstance(self, PipelinePhase):
            raise NotImplementedError('Method of an abstract class')
        instruction_to_pass = self.current_instruction
        self.current_instruction = NOP()
        return instruction_to_pass

class PipelinePhaseIF(PipelinePhase):
    
    def __init__(self):
        super(PipelinePhaseIF, self).__init__()
    
    def action(self):
        if isinstance(self.current_instruction, NOP):
            opcode = self.current_instruction.code[0:6]
            if opcode == '000000':
                funct = self.current_instruction.code[-6:]
                
            elif opcode == '001000':
                pass


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
    
    def action(self, id_phase, PC_counter):
        if isinstance(self.current_instruction, NOP):
            self.current_instruction = id_phase.try_to_return_instruction()
        self.current_instruction.action_EX(PC_counter) 
        
    def try_to_return_instruction(self):
        if self.current_instruction.is_finished():
            return PipelinePhase.try_to_return_instruction(self)
        else:
            return NOP()
            

class PipelinePhaseMEM(PipelinePhase):
    
    def __init__(self):
        super(PipelinePhaseMEM, self).__init__()

    def action(self, ex_phase, memX, memY):       
        self.current_instruction = ex_phase.try_to_return_instruction()
        self.current_instruction.action_MEM(memX, memY)
    

class PipelinePhaseWB(PipelinePhase):
    
    def __init__(self):
        super(PipelinePhaseWB, self).__init__()

    def action(self, mem_phase, registers):
        self.current_instruction = mem_phase.try_to_return_instruction()
        self.current_instruction.action_WB(registers)
    

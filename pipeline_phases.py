# coding: utf-8

from instructions import NOP


class PipelinePhase(object):
    def __init__(self):
        self.current_phase = NOP()
        
    def action(self):
        raise NotImplementedError('Method from an abstract class')
    
    def try_to_get_instruction(self):
        raise NotImplementedError('Method from an abstract class')


class PipelinePhaseIF(PipelinePhase):
    
    def __init__(self):
        super(PipelinePhaseIF, self).__init__()
    
    def action(self):
        pass


class PipelinePhaseID(PipelinePhase):
    
    def __init__(self):
        super(PipelinePhaseID, self).__init__()

    def action(self, if_phase, registers):
        if isinstance(self.current_instruction, NOP):
            self.current_instruction = if_phase.try_to_get_instruction()
        self.current_instruction.action_ID(registers)


class PipelinePhaseEX(PipelinePhase):
    
    def __init__(self):
        super(PipelinePhaseEX, self).__init__()
    
    def action(self, id_phase):
        if isinstance(self.current_instruction, NOP):
            self.current_instruction = id_phase.try_to_get_instruction()
        self.current_instruction.action_EX() 

class PipelinePhaseMEM(PipelinePhase):
    
    def __init__(self):
        super(PipelinePhaseMEM, self).__init__()

    def action(self, ex_phase, memX, memY):
        if isinstance(self.current_instruction, NOP):
            self.current_instruction = ex_phase.try_to_get_instruction()
        self.current_instruction.action_MEM()
    

class PipelinePhaseWB(PipelinePhase):
    
    def __init__(self):
        super(PipelinePhaseWB, self).__init__()

    def action(self, mem_phase, registers):
        if isinstance(self.current_instruction, NOP):
            self.current_instruction = mem_phase.try_to_get_instruction()
        self.current_instruction.action_WB()
    

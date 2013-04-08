# coding: utf-8

from instructions import NOP


class PipelinePhase(object):
    def __init__(self):
        self.current_phase = NOP()


class PipelinePhaseIF(PipelinePhase):
    
    def __init__(self):
        super(PipelinePhaseIF, self).__init__()
    
    def action(self):
        pass


class PipelinePhaseID(PipelinePhase):
    
    def __init__(self):
        super(PipelinePhaseID, self).__init__()

    def action(self, first_phase, registers):
        self.current_instruction = first_phase.current_instruction
        self.current_instruction.action_ID(registers)


class PipelinePhaseEX(PipelinePhase):
    
    def __init__(self):
        super(PipelinePhaseEX, self).__init__()
    
    def action(self):
        pass
#        if isinstance(self.current_instruction, instructions.MUL):
#            if True:
#                pass    

class PipelinePhaseMEM(PipelinePhase):
    
    def __init__(self):
        super(PipelinePhaseMEM, self).__init__()

    def action(self):
        pass
    

class PipelinePhaseWB(PipelinePhase):
    
    def __init__(self):
        super(PipelinePhaseWB, self).__init__()

    def action(self):
        pass
    

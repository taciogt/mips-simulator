# coding: utf-8

import instructions.NOP, instructions.MUL


class PipelinePhase:
    def __init__(self):
        self.current_phase = instructions.NOP()


class PipelinePhaseIF(PipelinePhase):
    
    current_instruction = None
    def action(self):
        pass


class PipelinePhaseID:

    def action(self, phase, registers):
        self.current_instruction = phase.current_instruction
        self.current_instruction.action_ID(registers)


class PipelinePhaseEX():
    
    def action(self):
        if isinstance(self.current_instruction, instructions.MUL):
            if True:
                pass    

class PipelinePhaseMEM():

    def action(self):
        pass
    

class PipelinePhaseWB():

    def action(self):
        pass
    

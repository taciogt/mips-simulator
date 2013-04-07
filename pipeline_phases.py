# coding: utf-8

import instructions.NOP, instructions.MUL


class PipelinePhaseIF():
    current_instruction = None
    def action();
        pass

class PipelinePhaseID():
    self.current_instruction = None

    def action(self, phase, registers):
        self.current_instruction = phase.current_instruction
        self.current_instruction.action_ID(registers)


class PipelinePhaseEX():
    self.current_instruction = Instruction.NOP()
    
    def action(self):
        if isinstance(self.current_instruction, Instruction.MUL):
            if True:
                pass    

class PipelinePhaseMEM():
    current_instruction = None
    def action();
        pass
    

class PipelinePhaseWB():
    current_instruction = None
    def action();
        pass
    
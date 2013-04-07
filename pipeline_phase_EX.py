# coding: utf-8

import Instruction.NOP, Instruction.MUL


class PipelinePhaseEX():
    self.current_instruction = Instruction.NOP()
    
    def action(self):
        if isinstance(self.current_instruction, Instruction.MUL):
            if
    

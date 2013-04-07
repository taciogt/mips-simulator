# coding: utf-8

class PipelinePhaseID():
	self.current_instruction = None

	def action(self, phase, registers):
	    self.current_instruction = phase.current_instruction
	    self.current_instruction.action_ID(registers)

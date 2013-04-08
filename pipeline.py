# coding: utf-8

class Pipeline(object):
	
	def __init__(self):
	
	    self.registers = []
	    for i in range(32):
		    self.registers.append(Register())
	
	    self.phase = []
	    self.phase.append(PipelinePhaseIF())
	    self.phase.append(PipelinePhaseID())
	    self.phase.append(PipelinePhaseEX())
	    self.phase.append(PipelinePhaseMEM())
	    self.phase.append(PipelinePhaseWB())
	
	    self.memX = []
	    self.memY = []
	
	    self.dados = []
	
	    self.PC = []
	    self.PC_counter = 0
	
	    control_signals = {"RegDst":0,
                           "ALUSrc":0,
                           "MemtoReg":0,
                           "RegWrite":0,
                           "MemWrite":0,
                           "Branch":0,
                           "Jump":0,
                           "ExtOp":0}
	

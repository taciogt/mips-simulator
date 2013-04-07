# coding: utf-8

class Pipeline(object):
	
	
	registers = []
	for i in range(32):
		registers.append(Register())
	
	phase = []
	phase.append(PipelinePhaseIF())
	phase.append(PipelinePhaseID())
	phase.append(PipelinePhaseEX())
	phase.append(PipelinePhaseMEM())
	phase.append(PipelinePhaseWB())
	
	memX = []
	memY = []
	
	dados = []
	
	PC = []
	PC_counter = 0
	
	controlSignals = {}
	controlSignals["RegDst"]=0
	controlSignals["ALUSrc"]=0
	controlSignals["MemtoReg"]=0
	controlSignals["RegDst"]=0
	controlSignals["RegDst"]=0
	controlSignals["RegDst"]=0
	controlSignals["RegDst"]=0
	
	#def __init__ (self, )

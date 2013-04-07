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
	controlSignals["RegDst"] = 0
	controlSignals["ALUSrc"] = 0
	controlSignals["MemtoReg"] = 0
	controlSignals["RegWrite"] = 0
	controlSignals["MemWrite"] = 0
	controlSignals["Branch"] = 0
	controlSignals["Jump"] = 0
	controlSignals["ExtOp"] = 0
	controlSignals["ALUctr<2:0>"] = None
	

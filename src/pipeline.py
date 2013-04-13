# coding: utf-8
from register import Register
from pipeline_phases import *


class Pipeline(object):

    def __init__(self):

        self.registers = []
        for i in range(32):
            self.registers.append(Register())

        self.phases = []
        self.phases.append(PipelinePhaseIF())
        self.phases.append(PipelinePhaseID())
        self.phases.append(PipelinePhaseEX())
        self.phases.append(PipelinePhaseMEM())
        self.phases.append(PipelinePhaseWB())

        self.mem = []

        self.PC = []
        self.PC_counter = Register()

# coding: utf-8

from threading import Thread
from pipeline import *
from register import *
import time


def printPhases(phases):
    for i in range(0, 5):
        print str(phases[i].current_instruction)


class ProgramController(object):

    def __init__(self):
        self.pipeline = Pipeline()
        self.clock_number = 0
        self.finished_instructions = [0]
        self.recently_used_mem = [0, 0, 0, 0]
        self.should_pause = True
        self.pipeline.PC = []
        self.interface = None

    def all_phases_NOP(self, phases):
        res = True
        for i in range(0, 5):
            res = res and isinstance(phases[i].current_instruction, NOP)
        return res

    def one_clock(self, phases):
        self.clock_number += 1

        # this variable is important not to update pipeline values with
        # 'should_pause' set to True (this condition avoid recursion, but
        # run_clock() executes one last time)
        if self.update_pipeline:
            self.run_pipeline_phases(phases)

        self.interface.update_interface()

    #this method should be called only by run_one_clock
    #and by run_clocks_continuously
    def run_clock(self, phases):
        while not self.should_pause:
            #time.sleep(0.001)
            self.one_clock(phases)

        # if not self.should_pause:

    def run_pipeline_phases(self, phases):
        #run all phases of pipeline. It is not a loop because
        #we decided to make different signatures for each one
        phases[4].action(
            self.pipeline.phases[3],
            self.pipeline.registers,
            self.finished_instructions)
        phases[3].action(
            self.pipeline.phases[2],
            self.pipeline.mem,
            self.pipeline.PC_counter,
            self.pipeline.recently_used_mem)
        phases[2].action(self.pipeline.phases[1])
        phases[1].action(self.pipeline.phases[0], self.pipeline.registers)
        phases[0].action(self.pipeline.PC, self.pipeline.PC_counter, self.pipeline.registers)

        #this is here for debugging
        print self.clock_number
        print "=========="
        printPhases(phases)
        print "=========="

        #stop condition
        if (self.pipeline.PC_counter.get_value() >= len(self.pipeline.PC)) and self.all_phases_NOP(phases):
            self.should_pause = True

    def run_one_clock(self):
        self.update_pipeline = True
        self.should_pause = True
        t = Thread(target=self.one_clock, args=(self.pipeline.phases,))
        t.start()

    def run_clocks_continuously(self):
        self.update_pipeline = True
        self.should_pause = False
        t = Thread(target=self.run_clock, args=(self.pipeline.phases,))
        t.start()

    def pause(self):
        self.should_pause = True
        self.update_pipeline = False

    def openFile(self):
        pass

    #Contains the last four adresses used in memory

    #deletes the oldest memory from our list and adds
    #a new one. This is used by the GUI to know which
    #were the last 4 used memory adresses and to get their
    #values (so that they can be shown)
    def add_used_mem(self, mem_address):
        del recently_used_mem[0]
        recently_used.append(mem_address)

    def get_productivity(self):
        return float(self.finished_instructions[0])/self.clock_number

    def get_pipeline_phases_current_instruction(self):
        address = self.pipeline.PC_counter.get_value() / 4

        cur_inst_0 = self.pipeline.phases[0].current_instruction
        if isinstance(cur_inst_0, NOP):
            if address < len(self.pipeline.PC):
                cur_inst_0 = self.pipeline.phases[0].instantiate_instruction(
                    self.pipeline.PC[address])

        return [
            str(cur_inst_0),
            str(self.pipeline.phases[1].current_instruction),
            str(self.pipeline.phases[2].current_instruction),
            str(self.pipeline.phases[3].current_instruction),
            str(self.pipeline.phases[4].current_instruction),
        ]

    def get_pipeline_registers_value(self):
        values = []
        for register in self.pipeline.registers:
            values.append(register.get_value())
        return values

    def get_pipeline_phases_control_signals(self):
        return [
            self.pipeline.phases[2].current_instruction.get_control_signals(),
            self.pipeline.phases[3].current_instruction.get_control_signals(),
            self.pipeline.phases[4].current_instruction.get_control_signals(),
        ]

    def get_recent_memory(self):
        return self.pipeline.recently_used_mem

    def get_information(self):
        info_dict = {
            'clock_number': self.clock_number,
            'pc': self.pipeline.PC_counter.get_value(),
            'finished_instructions': self.finished_instructions[0],
            'productivity': self.get_productivity(),
        }
        return info_dict

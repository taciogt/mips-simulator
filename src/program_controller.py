# coding: utf-8

from threading import Thread
from pipeline import *
from register import *


def printPhases(phases):
    for i in range(0, 5):
        print str(phases[i].current_instruction)


class ProgramController(object):

    def __init__(self):
        self.pipeline = Pipeline()
        self.clock_number = 0
        self.finished_instructions = 0
        self.recently_used_mem = [0, 0, 0, 0]
        self.should_pause = True
        self.pipeline.PC = []

    def all_phases_NOP(self, phases):
        res = True
        for i in range(0, 5):
            res = res and isinstance(phases[i].current_instruction, NOP)
        return res

    #this method should be called only by run_one_clock
    #and by run_clocks_continuously
    def run_clock(self, phases):
        self.clock_number += 1

        #run all phases of pipeline. It is not a loop because
        #we decided to make different signatures for each one
        phases[4].action(self.pipeline.phases[3], self.pipeline.registers)
        phases[3].action(self.pipeline.phases[2], self.pipeline.mem, self.pipeline.PC_counter)
        phases[2].action(self.pipeline.phases[1])
        phases[1].action(self.pipeline.phases[0], self.pipeline.registers)
        phases[0].action(self.pipeline.PC, self.pipeline.PC_counter, self.pipeline.registers)

        #this is here for debugging
        print self.clock_number
        print "=========="
        print self.pipeline.registers[2].get_value()
        printPhases(phases)
        print "=========="

        #stop condition
        if (self.pipeline.PC_counter.get_value() >= len(self.pipeline.PC)) and self.all_phases_NOP(phases):
            self.should_pause = True
        if not self.should_pause:
            self.run_clock(phases)

    def run_one_clock(self):
        self.should_pause = True
        t = Thread(target=self.run_clock, args=(self.pipeline.phases,))
        t.start()

    def run_clocks_continuously(self):
        self.should_pause = False
        t = Thread(target=self.run_clock, args=(self.pipeline.phases,))
        t.start()

    def pause(self):
        self.should_pause = True

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
        return finished_instructions/clock_number

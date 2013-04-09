# coding: utf-8

class Loader(object):
    def __init__(self):
        self.pc = []
        self.mem_x = []
        self.mem_y = []
        self.instruction_lines = []

    def read_instructions(self):
        f = open('instructions.txt','r')
        for line in f:
            self.instruction_lines.append(line)
        f.close()

    def load_pc(self):
        for line in self.instruction_lines:
            inst_code = line.split()[0]
            self.pc.append(inst_code)

    def get_pc(self):
        self.read_instructions()
        self.load_pc()
        return self.pc

    def read_mem_values(self):
        f = open('../mem.txt','r')
        for line in f:
            x, y = line.split()
            self.mem_x.append(x)
            self.mem_y.append(y)

    def get_mem_x(self):
        return self.mem_x

    def get_mem_y(self):
        return self.mem_y
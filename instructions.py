# coding: utf-8
from bitstring import BitArray

class Instruction():
    
    def get_register_position(self, start, end):
        
        if start == 0:
            b = BitArray(self.code[-end:])
            return b.uint
        else:
            b = BitArray(self.code[-end:-start])
            return b.uint

    def get_immediate_value(self):
        
        b = BitArray(self.code[-16:])
        return b.int


    def action_ID(self):
        raise NotImplementedError('This is an abstract class.')

    def action_EX(self):
        raise NotImplementedError('This is an abstract class.')

    def action_MEM(self):
        raise NotImplementedError('This is an abstract class.')

    def action_WB(self):
        raise NotImplementedError('This is an abstract class.')                
     
     
class NOP(Instruction):
    pass
       
# Instrucao vai ser Rd = Rs + Rt
class ADD(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code
        
    def action_ID(self, registers):
        # 26 to 21
        self.Rs = registers[self.get_register_position(21, 26)].value
        # 21 to 16
        self.Rt = registers[self.get_register_position(16, 21)].value
        
    def action_EX(self):
        self.Rd = self.Rs + self.Rt
        
    def action_MEM(self, memX, memY):
        pass
        
    def action_WB(self, registers):
        # Rd: 16 to 11
        registers[self.get_register_position(11, 16)] = self.Rd
        
    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor
    def get_control_signals(self):    
        control_signals = {"RegDst":1,
                            "ALUSrc":0,
                            "MemtoReg":0,
                            "RegWrite":1,
                            "MemWrite":0,
                            "Branch":0,
                            "Jump":0,
                            "ExtOp":None}
        return control_signals

class ADDi(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code
        
    def action_ID(self, registers):
        # 26 to 21
        self.Rs = registers[self.get_register_position(21, 26)].value
        # 16 to 0
        self.ImmExt = self.get_immediate_value()
        
    def action_EX(self):
        if ()
        self.Rd = self.Rs + self.Rt
        
    def action_MEM(self, memX, memY):
        pass
        
    def action_WB(self, registers):
        # Rd: 16 to 11
        registers[self.get_register_position(11, 16)] = self.Rd
        
    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor
    def get_control_signals(self):    
        control_signals = {"RegDst":1,
                            "ALUSrc":0,
                            "MemtoReg":0,
                            "RegWrite":1,
                            "MemWrite":0,
                            "Branch":0,
                            "Jump":0,
                            "ExtOp":None}
        return get_control_signals

# Instrucao vai ser Rd = Rs - Rt
class SUB(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code
        
    def action_ID(self, registers):
        # 26 to 21
        self.Rs = registers[self.get_register_position(21, 26)].value
        # 21 to 16
        self.Rt = registers[self.get_register_position(16, 21)].value
        
    def action_EX(self):
        self.Rd = self.Rs - self.Rt
        
    def action_MEM(self, memX, memY):
        pass
        
    def action_WB(self, registers):
        # Rd: 16 to 11
        registers[self.get_register_position(11, 16)] = self.Rd
        
    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor
    def get_control_signals(self):    
        control_signals = {"RegDst":0,
                            "ALUSrc":0,
                            "MemtoReg":0,
                            "RegWrite":1,
                            "MemWrite":0,
                            "Branch":0,
                            "Jump":0,
                            "ExtOp":None}
        return control_signals

# Instrucao vai ser Rd = Rs*Rt
class MUL(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code
        
    def action_ID(self, registers):
        # 26 to 21
        self.Rs = registers[self.get_register_position(21, 26)].value
        # 21 to 16
        self.Rt = registers[self.get_register_position(16, 21)].value
        
    def action_EX(self):
        self.Rd = self.Rs*self.Rt
        
    def action_MEM(self, memX, memY):
        pass
        
    def action_WB(self, registers):
        # Rd: 16 to 11
        registers[self.get_register_position(11, 16)] = self.Rd
        
    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor
    def get_control_signals(self):    
        control_signals = {"RegDst":0,
                            "ALUSrc":0,
                            "MemtoReg":0,
                            "RegWrite":1,
                            "MemWrite":0,
                            "Branch":0,
                            "Jump":0,
                            "ExtOp":None}
        return control_signals

# Instrucao vai ser Rd = Rs*Rt
class BEQ(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code
        
    def action_ID(self, registers):
        # 26 to 21
        self.Rs = registers[self.get_register_position(21, 26)].value
        # 21 to 16
        self.Rt = registers[self.get_register_position(16, 21)].value
        
    def action_EX(self, PC_counter):
        #if self.Rs==self.Rt:
        pass
             
        
    def action_MEM(self, memX, memY):
        pass
        
    def action_WB(self, registers):
        # Rd: 16 to 11
        registers[self.get_register_position(11, 16)] = self.Rd
        
    # Returns a dictionary with the control signal names as keys and
    # the bits (0 or 1) as values.
    # These bits should be looked at the third pipeline PDF from the Professor
    def get_control_signals(self):    
        control_signals = {"RegDst":0,
                            "ALUSrc":0,
                            "MemtoReg":0,
                            "RegWrite":1,
                            "MemWrite":0,
                            "Branch":0,
                            "Jump":0,
                            "ExtOp":None}
        return control_signals

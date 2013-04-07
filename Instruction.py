class Instruction():

    code = ""
    
    def get_register_position(self, start, end):
        if start == 0:
            return int(("0b"+self.code[-end:]),2)
        else:
            return int(("0b"+self.code[-end:-start]),2)
        
    def action_ID():
        pass

    def action_EX():
        pass

    def action_MEM():
        pass        

    def action_WB():
        pass                
        
#Instrucao vai ser Rd = Rs + Rt
class Instruction_ADD(Instruction):

    def __init__(self, instruction_code):
        self.code = instruction_code
        
    def action_ID(self, registers):
        #26 to 21
        self.Rs = registers[self.get_register_position(21,26)].value
        #21 to 16
        self.Rt = registers[self.get_register_position(16,21)].value
        
    def action_EX(self):
        self.Rd = self.Rs + self.Rt
        
    def action_MEM(self):
        pass
        
    def action_WB(self,registers):
        #Rd: 16 to 11
        registers[self.get_register_position(11,16)] = self.Rd
        
    #Returns a dictionary with the control signal names as keys and
    #the bits (0 or 1) as values.
    #These bits should be looked at the third pipeline PDF from the Professor
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

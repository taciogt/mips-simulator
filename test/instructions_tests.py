# coding: utf-8

import unittest
from instructions import *

class InstructionsTests(unittest.TestCase):
    def test_not_implemented_methods(self):
        instruction = Instruction()
        self.assertRaises(NotImplementedError, instruction.action_ID)
        self.assertRaises(NotImplementedError, instruction.action_EX)
        self.assertRaises(NotImplementedError, instruction.action_MEM)
        self.assertRaises(NotImplementedError, instruction.action_WB)
        
    def test_add_instruction(self):
        op = '000000'
        rs = '10011' # Rs -->19 
        rt = '01100' # Rt --> 12
        rd = '11001' # Rd --> 25
        shamt = '000000'
        funct = '100000'
        code = op + rs + rt + rd + shamt + funct
        
        registers = [0] * 32
        registers[19] = 1
        registers[12] = 2
        
        instruction = ADD(code)
        instruction.action_ID(registers)
        
        self.assertEqual(instruction.Rs, 1)
        self.assertEqual(instruction.Rt, 2)
        
        instruction.action_EX()
        self.assertEqual(instruction.Rd, 3)
        
        instruction.action_WB(registers)
        instruction.assertEqual(registers[25], 3)

    # lembrar de testar para complemento de 2!
    def test_add_i(self):
        pass
        
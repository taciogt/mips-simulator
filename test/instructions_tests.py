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

# coding: utf-8

import unittest
from pipeline_phases import *
import instructions


class PipelinePhasesTests(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.pipelines = [PipelinePhaseIF(), PipelinePhaseID(), PipelinePhaseEX(), PipelinePhaseMEM(), PipelinePhaseWB()]

    def test_not_implemented_method(self):
        self.assertRaises(NotImplementedError, PipelinePhase().action)
        self.assertRaises(NotImplementedError, PipelinePhase().try_to_return_instruction)

    

    def test_nop_as_default(self):
        for p in self.pipelines:
            self.assertTrue(isinstance(p.current_instruction, instructions.NOP))

    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
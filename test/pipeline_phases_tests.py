# coding: utf-8

import unittest
from pipeline_phases import *
import instructions


class PipelinePhasesTests(unittest.TestCase):

    def test_nop_as_default(self):
        pipelines = [PipelinePhaseIF(), PipelinePhaseID(), PipelinePhaseEX(), PipelinePhaseMEM(), PipelinePhaseWB()]
        for p in pipelines:
            self.assertTrue(isinstance(p.current_phase, instructions.NOP))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
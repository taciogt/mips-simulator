import sys
sys.path.append("../")
import program_controller
from program_controller import ProgramController

controller = ProgramController()
controller.run_clocks_continuously()

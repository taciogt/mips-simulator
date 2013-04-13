# coding: utf-8
import sys
sys.path.append("../")
from src.program_controller import ProgramController
from src.loader import Loader

controller = ProgramController()
l = Loader()
l.read_mem_values()
controller.pipeline.mem = l.get_mem_x()
controller.pipeline.mem.extend(l.get_mem_y())

controller.pipeline.PC = ["00100000000000100000000000000010",
                          "00100000000001010000001111101000",
                          "00100000000001100001001110001000",
                          "00100000000000010000000000000000",
                          "00100000000001110000000000000100",
                          "10001100101011110000000000000000",
                          "00000001111000100111100000011000",
                          "10001100110100000000000000000000",
                          "00000001111100001000000000100000",
                          "10101100110100000000000000000000",
                          "00100000001000010000000000000001",
                          "00100000101001010000000000000100",
                          "00100000110001100000000000000100",
                          "00011100001001110000000000010100"]
                          

controller.run_clocks_continuously()


#00100000000001110000001111101000
#LI R2,2 ; A         ; "001000 00000 00010 0000000000000010"
#LI R5,1000 ; X      ; "001000 00000 00101 0000001111101000"
#LI R6,5000 ; Y      ; "001000 00000 00110 0001001110001000"
#LI R1,0 ; I         ; "001000 00000 00001 0000000000000000"
#LI R7,1000          ; "001000 00000 00111 0000001111101000"
#LOOP: 
#LW R15,0(R5)        ; "100011 00101 01111 0000000000000000"
#MUL R15,R15,R2      ; "000000 01111 00010 01111 00000 011000"
#LW R16,0(R6)        ; "100011 00110 10000 0000000000000000"
#ADD R16,R15,R16     ; "000000 01111 10000 10000 00000 100000"
#SW R16,0(R6)        ; "101011 00110 10000 0000000000000000"
#ADDI R1,R1,1        ; "001000 00001 00001 0000000000000001"
#ADDI R5,R5,4        ; "001000 00101 00101 0000000000000100"
#ADDI R6,R6,4        ; "001000 00110 00110 0000000000000100"
#BLE R1,R7,LOOP(20)  ; "000111 00001 00111 0000000000010100"


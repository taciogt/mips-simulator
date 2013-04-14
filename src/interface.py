# coding: utf-8
import Tkinter as tk
from program_controller import ProgramController
from loader import Loader
import time


class Interface(tk.Tk):
    def __init__(self, controller):
        tk.Tk.__init__(self)
        self.title("MIPS Simulator")
        self.controller = controller
        # Quadro superior

        self.label_instrucao_if = tk.Label(self, text="Id. Inst. em IF")
        self.instrucao_if = tk.StringVar()
        self.value_instrucao_if = tk.Label(
            self,
            textvariable=self.instrucao_if)
        self.label_instrucao_di_rf = tk.Label(self, text="Id. Inst. em DI/RF")
        self.instrucao_di_rf = tk.StringVar()
        self.value_instrucao_di_rf = tk.Label(
            self,
            textvariable=self.instrucao_di_rf)
        self.label_instrucao_ex = tk.Label(self, text="Id. Inst. em EX")
        self.instrucao_ex = tk.StringVar()
        self.value_instrucao_ex = tk.Label(
            self,
            textvariable=self.instrucao_ex)
        self.label_instrucao_mem = tk.Label(self, text="Id. Inst. em MEM")
        self.instrucao_mem = tk.StringVar()
        self.value_instrucao_mem = tk.Label(
            self,
            textvariable=self.instrucao_mem)
        self.label_instrucao_wb = tk.Label(self, text="Id. Inst. em WB")
        self.instrucao_wb = tk.StringVar()
        self.value_instrucao_wb = tk.Label(
            self,
            textvariable=self.instrucao_wb)
        self.label_instrucao_if.grid(row=0, column=0)
        self.label_instrucao_di_rf.grid(row=0, column=1)
        self.label_instrucao_ex.grid(row=0, column=2, columnspan=2)
        self.label_instrucao_mem.grid(row=0, column=4, columnspan=2)
        self.label_instrucao_wb.grid(row=0, column=6, columnspan=2)
        self.value_instrucao_if.grid(row=1, column=0)
        self.value_instrucao_di_rf.grid(row=1, column=1)
        self.value_instrucao_ex.grid(row=1, column=2, columnspan=2)
        self.value_instrucao_mem.grid(row=1, column=4, columnspan=2)
        self.value_instrucao_wb.grid(row=1, column=6, columnspan=2)

        self.label_reg_dst = tk.Label(self, text="RegDst")
        self.reg_dst = tk.StringVar()
        self.value_reg_dst = tk.Label(self, textvariable=self.reg_dst)
        self.label_alu_op1 = tk.Label(self, text="ALUOp1")
        self.alu_op1 = tk.StringVar()
        self.value_alu_op1 = tk.Label(self, textvariable=self.alu_op1)
        self.label_alu_op2 = tk.Label(self, text="ALUOp2")
        self.alu_op2 = tk.StringVar()
        self.value_alu_op2 = tk.Label(self, textvariable=self.alu_op2)
        self.label_alu_src = tk.Label(self, text="ALUSrc")
        self.alu_src = tk.StringVar()
        self.value_alu_src = tk.Label(self, textvariable=self.alu_src)
        self.label_reg_dst.grid(row=2, column=2)
        self.label_alu_op1.grid(row=3, column=2)
        self.label_alu_op2.grid(row=4, column=2)
        self.label_alu_src.grid(row=5, column=2)
        self.value_reg_dst.grid(row=2, column=3)
        self.value_alu_op1.grid(row=3, column=3)
        self.value_alu_op2.grid(row=4, column=3)
        self.value_alu_src.grid(row=5, column=3)

        self.label_branch = tk.Label(self, text="Branch")
        self.branch = tk.StringVar()
        self.value_branch = tk.Label(self, textvariable=self.branch)
        self.label_mem_read = tk.Label(self, text="MemRead")
        self.mem_read = tk.StringVar()
        self.value_mem_read = tk.Label(self, textvariable=self.mem_read)
        self.label_mem_write = tk.Label(self, text="MemWrite")
        self.mem_write = tk.StringVar()
        self.value_mem_write = tk.Label(self, textvariable=self.mem_write)
        self.label_branch.grid(row=2, column=4)
        self.label_mem_read.grid(row=3, column=4)
        self.label_mem_write.grid(row=4, column=4)
        self.value_branch.grid(row=2, column=5)
        self.value_mem_read.grid(row=3, column=5)
        self.value_mem_write.grid(row=4, column=5)

        self.label_reg_write = tk.Label(self, text="RegWrite")
        self.reg_write = tk.StringVar()
        self.value_reg_write = tk.Label(self, textvariable=self.reg_write)
        self.label_mem_to_reg = tk.Label(self, text="MemToReg")
        self.mem_to_reg = tk.StringVar()
        self.value_mem_to_reg = tk.Label(self, textvariable=self.mem_to_reg)
        self.label_reg_write.grid(row=2, column=6)
        self.label_mem_to_reg.grid(row=3, column=6)
        self.value_reg_write.grid(row=2, column=7)
        self.value_mem_to_reg.grid(row=3, column=7)

        # Figura

        self.image = tk.PhotoImage(file='pipeline.gif')
        self.label_image = tk.Label(self, image=self.image)
        self.label_image.grid(row=7, column=0, rowspan=19, columnspan=8)

        # Quadro dos botões

        self.button_play = tk.Button(self, text="Play")
        self.button_play.grid(row=0, rowspan=6, column=8, columnspan=2)
        self.button_ff = tk.Button(self, text="Run")
        self.button_ff.grid(row=0, rowspan=6, column=10, columnspan=2)
        self.button_pause = tk.Button(self, text="Pause")
        self.button_pause.grid(row=0, rowspan=6, column=12, columnspan=2)
        self.button_open = tk.Button(self, text="Open")
        self.button_open.grid(row=0, rowspan=6, column=14, columnspan=2)

        # Quadros ao lado direito da figura

        self.label_mem_rec_usada = tk.Label(
            self,
            text="Memória recentemente usada")
        self.label_endereco = tk.Label(self, text="Endereço")
        self.label_valor = tk.Label(self, text="Valor")

        # Binding dos botões

        self.bind("<Button-1>", lambda *ignore: self.setInstructions())
        self.setInstructions()

    def setInstructions(self):
        self.controller.run_one_clock()
        time.sleep(0.01)
        self.instrucao_if.set(str(self.controller.pipeline.phases[0].current_instruction))
        self.instrucao_di_rf.set(str(self.controller.pipeline.phases[1].current_instruction))
        self.instrucao_ex.set(str(self.controller.pipeline.phases[2].current_instruction))
        self.instrucao_mem.set(str(self.controller.pipeline.phases[3].current_instruction))
        self.instrucao_wb.set(str(self.controller.pipeline.phases[4].current_instruction))


def main():
    controller = ProgramController()
    interface = Interface(controller)
    l = Loader()
    l.read_mem_values()
    controller.pipeline.mem = l.get_mem_x()
    controller.pipeline.mem.extend(l.get_mem_y())
    controller.pipeline.PC = ["00100000000000100000000000000010",
                              "00100000000001010000001111101000",
                              "00100000000001100001001110001000",
                              "00100000000000010000000000000000",
                              "00100000000001110000001111101000",
                              "10001100101011110000000000000000",
                              "00000001111000100111100000011000",
                              "10001100110100000000000000000000",
                              "00000001111100001000000000100000",
                              "10101100110100000000000000000000",
                              "00100000001000010000000000000001",
                              "00100000101001010000000000000100",
                              "00100000110001100000000000000100",
                              "00011100001001110000000000010100"]
    interface.mainloop()


if __name__ == '__main__':
    main()

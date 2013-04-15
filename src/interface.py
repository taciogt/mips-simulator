# coding: utf-8
import Tkinter as tk
from program_controller import ProgramController
from loader import Loader
from threading import Thread


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

        # >>> Quadros ao lado direito da figura <<<

        # Quadro dos botões

        self.button_play = tk.Button(self, text="Play")
        self.button_play.grid(row=0, rowspan=6, column=8, columnspan=2)
        self.button_ff = tk.Button(self, text="Run")
        self.button_ff.grid(row=0, rowspan=6, column=10, columnspan=2)
        self.button_pause = tk.Button(self, text="Pause")
        self.button_pause.grid(row=0, rowspan=6, column=12, columnspan=2)
        self.button_open = tk.Button(self, text="Open")
        self.button_open.grid(row=0, rowspan=6, column=14, columnspan=2)

        # Memória recentemente usada

        self.label_mem_rec_usada = tk.Label(
            self,
            text="Memória recentemente usada")
        self.label_endereco = tk.Label(self, text="Endereço")
        self.label_valor = tk.Label(self, text="Valor")
        self.end1 = tk.StringVar()
        self.label_end1 = tk.Label(self, textvariable=self.end1)
        self.end2 = tk.StringVar()
        self.label_end2 = tk.Label(self, textvariable=self.end2)
        self.end3 = tk.StringVar()
        self.label_end3 = tk.Label(self, textvariable=self.end3)
        self.end4 = tk.StringVar()
        self.label_end4 = tk.Label(self, textvariable=self.end4)
        self.valor_end1 = tk.StringVar()
        self.valor_end1 = tk.Label(self, textvariable=self.valor_end1)
        self.valor_end2 = tk.StringVar()
        self.valor_end2 = tk.Label(self, textvariable=self.valor_end2)
        self.valor_end3 = tk.StringVar()
        self.valor_end3 = tk.Label(self, textvariable=self.valor_end3)
        self.valor_end4 = tk.StringVar()
        self.valor_end4 = tk.Label(self, textvariable=self.valor_end4)
        self.label_mem_rec_usada.grid(row=6, column=8, columnspan=4)
        self.label_endereco.grid(row=7, column=8, columnspan=4)
        self.label_end1.grid(row=8, column=8, columnspan=4)
        self.label_end2.grid(row=9, column=8, columnspan=4)
        self.label_end3.grid(row=10, column=8, columnspan=4)
        self.label_end4.grid(row=11, column=8, columnspan=4)
        self.label_valor.grid(row=7, column=12, columnspan=4)
        self.valor_end1.grid(row=8, column=12, columnspan=4)
        self.valor_end2.grid(row=9, column=12, columnspan=4)
        self.valor_end3.grid(row=10, column=12, columnspan=4)
        self.valor_end4.grid(row=11, column=12, columnspan=4)

        # Informações

        self.label_clock = tk.Label(self, text="Clock corrente")
        self.label_pc = tk.Label(self, text="PC")
        self.label_inst_concluidas = tk.Label(
            self, text="Número de instruções concluidas")
        self.label_produtividade = tk.Label(
            self, text="Produtividade do pipeline")
        self.clock = tk.StringVar()
        self.value_clock = tk.Label(self, textvariable=self.clock)
        self.pc = tk.StringVar()
        self.value_pc = tk.Label(self, textvariable=self.pc)
        self.inst_concluidas = tk.StringVar()
        self.value_inst_concluidas = tk.Label(
            self, textvariable=self.inst_concluidas)
        self.produtividade = tk.StringVar()
        self.value_produtividade = tk.Label(
            self, textvariable=self.produtividade)
        self.label_clock.grid(row=12, column=8, columnspan=4)
        self.label_pc.grid(row=13, column=8, columnspan=4)
        self.label_inst_concluidas.grid(row=14, column=8, columnspan=4)
        self.label_produtividade.grid(row=15, column=8, columnspan=4)
        self.value_clock.grid(row=12, column=12, columnspan=4)
        self.value_pc.grid(row=13, column=12, columnspan=4)
        self.value_inst_concluidas.grid(row=14, column=12, columnspan=4)
        self.value_produtividade.grid(row=15, column=12, columnspan=4)

        # Registradores

        self.label_r0 = tk.Label(self, text="R0")
        self.label_r1 = tk.Label(self, text="R1")
        self.label_r2 = tk.Label(self, text="R2")
        self.label_r3 = tk.Label(self, text="R3")
        self.label_r4 = tk.Label(self, text="R4")
        self.label_r5 = tk.Label(self, text="R5")
        self.label_r6 = tk.Label(self, text="R6")
        self.label_r7 = tk.Label(self, text="R7")
        self.label_r8 = tk.Label(self, text="R8")
        self.label_r9 = tk.Label(self, text="R9")
        self.label_r10 = tk.Label(self, text="R10")
        self.label_r11 = tk.Label(self, text="R11")
        self.label_r12 = tk.Label(self, text="R12")
        self.label_r13 = tk.Label(self, text="R13")
        self.label_r14 = tk.Label(self, text="R14")
        self.label_r15 = tk.Label(self, text="R15")
        self.label_r16 = tk.Label(self, text="R16")
        self.label_r17 = tk.Label(self, text="R17")
        self.label_r18 = tk.Label(self, text="R18")
        self.label_r19 = tk.Label(self, text="R19")
        self.label_r20 = tk.Label(self, text="R20")
        self.label_r21 = tk.Label(self, text="R21")
        self.label_r22 = tk.Label(self, text="R22")
        self.label_r23 = tk.Label(self, text="R23")
        self.label_r24 = tk.Label(self, text="R24")
        self.label_r25 = tk.Label(self, text="R25")
        self.label_r26 = tk.Label(self, text="R26")
        self.label_r27 = tk.Label(self, text="R27")
        self.label_r28 = tk.Label(self, text="R28")
        self.label_r29 = tk.Label(self, text="R29")
        self.label_r30 = tk.Label(self, text="R30")
        self.label_r31 = tk.Label(self, text="R31")
        self.label_r0.grid(row=17, column=8)
        self.label_r1.grid(row=18, column=8)
        self.label_r2.grid(row=19, column=8)
        self.label_r3.grid(row=20, column=8)
        self.label_r4.grid(row=21, column=8)
        self.label_r5.grid(row=22, column=8)
        self.label_r6.grid(row=23, column=8)
        self.label_r7.grid(row=24, column=8)
        self.label_r8.grid(row=17, column=10)
        self.label_r9.grid(row=18, column=10)
        self.label_r10.grid(row=19, column=10)
        self.label_r11.grid(row=20, column=10)
        self.label_r12.grid(row=21, column=10)
        self.label_r13.grid(row=22, column=10)
        self.label_r14.grid(row=23, column=10)
        self.label_r15.grid(row=24, column=10)
        self.label_r16.grid(row=17, column=12)
        self.label_r17.grid(row=18, column=12)
        self.label_r18.grid(row=19, column=12)
        self.label_r19.grid(row=20, column=12)
        self.label_r20.grid(row=21, column=12)
        self.label_r21.grid(row=22, column=12)
        self.label_r22.grid(row=23, column=12)
        self.label_r23.grid(row=24, column=12)
        self.label_r24.grid(row=17, column=14)
        self.label_r25.grid(row=18, column=14)
        self.label_r26.grid(row=19, column=14)
        self.label_r27.grid(row=20, column=14)
        self.label_r28.grid(row=21, column=14)
        self.label_r29.grid(row=22, column=14)
        self.label_r30.grid(row=23, column=14)
        self.label_r31.grid(row=24, column=14)
        self.r0 = tk.StringVar()
        self.r1 = tk.StringVar()
        self.r2 = tk.StringVar()
        self.r3 = tk.StringVar()
        self.r4 = tk.StringVar()
        self.r5 = tk.StringVar()
        self.r6 = tk.StringVar()
        self.r7 = tk.StringVar()
        self.r8 = tk.StringVar()
        self.r9 = tk.StringVar()
        self.r10 = tk.StringVar()
        self.r11 = tk.StringVar()
        self.r12 = tk.StringVar()
        self.r13 = tk.StringVar()
        self.r14 = tk.StringVar()
        self.r15 = tk.StringVar()
        self.r16 = tk.StringVar()
        self.r17 = tk.StringVar()
        self.r18 = tk.StringVar()
        self.r19 = tk.StringVar()
        self.r20 = tk.StringVar()
        self.r21 = tk.StringVar()
        self.r22 = tk.StringVar()
        self.r23 = tk.StringVar()
        self.r24 = tk.StringVar()
        self.r25 = tk.StringVar()
        self.r26 = tk.StringVar()
        self.r27 = tk.StringVar()
        self.r28 = tk.StringVar()
        self.r29 = tk.StringVar()
        self.r30 = tk.StringVar()
        self.r31 = tk.StringVar()
        self.value_r0 = tk.Label(self, textvariable=self.r0)
        self.value_r1 = tk.Label(self, textvariable=self.r1)
        self.value_r2 = tk.Label(self, textvariable=self.r2)
        self.value_r3 = tk.Label(self, textvariable=self.r3)
        self.value_r4 = tk.Label(self, textvariable=self.r4)
        self.value_r5 = tk.Label(self, textvariable=self.r5)
        self.value_r6 = tk.Label(self, textvariable=self.r6)
        self.value_r7 = tk.Label(self, textvariable=self.r7)
        self.value_r8 = tk.Label(self, textvariable=self.r8)
        self.value_r9 = tk.Label(self, textvariable=self.r9)
        self.value_r10 = tk.Label(self, textvariable=self.r10)
        self.value_r11 = tk.Label(self, textvariable=self.r11)
        self.value_r12 = tk.Label(self, textvariable=self.r12)
        self.value_r13 = tk.Label(self, textvariable=self.r13)
        self.value_r14 = tk.Label(self, textvariable=self.r14)
        self.value_r15 = tk.Label(self, textvariable=self.r15)
        self.value_r16 = tk.Label(self, textvariable=self.r16)
        self.value_r17 = tk.Label(self, textvariable=self.r17)
        self.value_r18 = tk.Label(self, textvariable=self.r18)
        self.value_r19 = tk.Label(self, textvariable=self.r19)
        self.value_r20 = tk.Label(self, textvariable=self.r20)
        self.value_r21 = tk.Label(self, textvariable=self.r21)
        self.value_r22 = tk.Label(self, textvariable=self.r22)
        self.value_r23 = tk.Label(self, textvariable=self.r23)
        self.value_r24 = tk.Label(self, textvariable=self.r24)
        self.value_r25 = tk.Label(self, textvariable=self.r25)
        self.value_r26 = tk.Label(self, textvariable=self.r26)
        self.value_r27 = tk.Label(self, textvariable=self.r27)
        self.value_r28 = tk.Label(self, textvariable=self.r28)
        self.value_r29 = tk.Label(self, textvariable=self.r29)
        self.value_r30 = tk.Label(self, textvariable=self.r30)
        self.value_r31 = tk.Label(self, textvariable=self.r31)
        self.value_r0.grid(row=17, column=9)
        self.value_r1.grid(row=18, column=9)
        self.value_r2.grid(row=19, column=9)
        self.value_r3.grid(row=20, column=9)
        self.value_r4.grid(row=21, column=9)
        self.value_r5.grid(row=22, column=9)
        self.value_r6.grid(row=23, column=9)
        self.value_r7.grid(row=24, column=9)
        self.value_r8.grid(row=17, column=11)
        self.value_r9.grid(row=18, column=11)
        self.value_r10.grid(row=19, column=11)
        self.value_r11.grid(row=20, column=11)
        self.value_r12.grid(row=21, column=11)
        self.value_r13.grid(row=22, column=11)
        self.value_r14.grid(row=23, column=11)
        self.value_r15.grid(row=24, column=11)
        self.value_r16.grid(row=17, column=13)
        self.value_r17.grid(row=18, column=13)
        self.value_r18.grid(row=19, column=13)
        self.value_r19.grid(row=20, column=13)
        self.value_r20.grid(row=21, column=13)
        self.value_r21.grid(row=22, column=13)
        self.value_r22.grid(row=23, column=13)
        self.value_r23.grid(row=24, column=13)
        self.value_r24.grid(row=17, column=15)
        self.value_r25.grid(row=18, column=15)
        self.value_r26.grid(row=19, column=15)
        self.value_r27.grid(row=20, column=15)
        self.value_r28.grid(row=21, column=15)
        self.value_r29.grid(row=22, column=15)
        self.value_r30.grid(row=23, column=15)
        self.value_r31.grid(row=24, column=15)

        # Binding dos botões

        self.bind("<Button-1>", lambda *ignore: self.setInstructions())
        self.setInstructions()

    def setInstructions(self):
        # Importante rodar essa parte em uma Thread para poder esperar o
        # self.controller.run_one_clock() terminar de atualizar as variáveis
        # antes de atualizar a interface (tava dando uns problemas de
        # sincronismo) e o join() faz isso.

        # t = Thread(target=self.controller.run_one_clock)
        # t.start()
        # t.join()

        # Pausando através do "time", apenas para testar

        self.controller.run_one_clock()
        import time
        time.sleep(0.01)

        pipeline_instructions = self.controller.get_pipeline_phases_current_instruction()

        self.instrucao_if.set(pipeline_instructions[0])
        self.instrucao_di_rf.set(pipeline_instructions[1])
        self.instrucao_ex.set(pipeline_instructions[2])
        self.instrucao_mem.set(pipeline_instructions[3])
        self.instrucao_wb.set(pipeline_instructions[4])

    def setRegisters(self):
        self.r0.set(
        self.r1.set(
        self.r2.set(
        self.r3.set(
        self.r4.set(
        self.r5.set(
        self.r6.set(
        self.r7.set(
        self.r8.set(
        self.r9.set(
        self.r10.set(
        self.r11.set(
        self.r12.set(
        self.r13.set(
        self.r14.set(
        self.r15.set(
        self.r16.set(
        self.r17.set(
        self.r18.set(
        self.r19.set(
        self.r20.set(
        self.r21.set(
        self.r22.set(
        self.r23.set(
        self.r24.set(
        self.r25.set(
        self.r26.set(
        self.r27.set(
        self.r28.set(
        self.r29.set(
        self.r30.set(
        self.r31.set(


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

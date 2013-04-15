# coding: utf-8
import Tkinter as tk
from program_controller import ProgramController
from loader import Loader


class Interface(tk.Tk):
    def __init__(self, controller):
        tk.Tk.__init__(self)
        self.title("MIPS Simulator")
        self.controller = controller
        self.controller.interface = self

        self.montar_quadro_superior()
        self.montar_figura()
        self.montar_quadro_botoes()
        self.montar_quadro_memoria()
        self.montar_informacoes_processador()
        self.montar_registradores()

    def montar_quadro_superior(self):
        # Quadro superior

        self.label_instrucao_if = tk.Label(
            self,
            text="Id. Inst. em IF",
            width=16)
        self.instrucao_if = tk.StringVar()
        self.value_instrucao_if = tk.Label(
            self,
            textvariable=self.instrucao_if)

        self.label_instrucao_di_rf = tk.Label(
            self,
            text="Id. Inst. em DI/RF",
            width=16)
        self.instrucao_di_rf = tk.StringVar()
        self.value_instrucao_di_rf = tk.Label(
            self,
            textvariable=self.instrucao_di_rf)

        self.label_instrucao_ex = tk.Label(
            self,
            text="Id. Inst. em EX",
            width=16)
        self.instrucao_ex = tk.StringVar()
        self.value_instrucao_ex = tk.Label(
            self,
            textvariable=self.instrucao_ex)

        self.label_instrucao_mem = tk.Label(
            self,
            text="Id. Inst. em MEM",
            width=16)
        self.instrucao_mem = tk.StringVar()
        self.value_instrucao_mem = tk.Label(
            self,
            textvariable=self.instrucao_mem)

        self.label_instrucao_wb = tk.Label(
            self,
            text="Id. Inst. em WB",
            width=16)
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

    def montar_figura(self):

        # Figura

        self.image = tk.PhotoImage(file='pipeline.gif')
        self.label_image = tk.Label(self, image=self.image)
        self.label_image.grid(row=7, column=0, rowspan=19, columnspan=8)

    # >>> Quadros ao lado direito da figura <<<

    def montar_quadro_botoes(self):
        # Quadro dos botões

        self.button_play = tk.Button(
            self,
            text="Play",
            width=10,
            command=self.run_one_clock)
        self.button_play.grid(row=0, rowspan=6, column=8, columnspan=2, padx=10)

        self.button_ff = tk.Button(
            self,
            text="Run",
            width=10,
            command=self.run_clocks_continuously)
        self.button_ff.grid(row=0, rowspan=6, column=10, columnspan=2, padx=10)

        self.button_pause = tk.Button(
            self,
            text="Pause",
            width=10,
            command=self.pause)
        self.button_pause.grid(row=0, rowspan=6, column=12, columnspan=2, padx=10)

        self.button_open = tk.Button(
            self,
            text="Open",
            width=10)
        self.button_open.grid(row=0, rowspan=6, column=14, columnspan=2, padx=10)

    def montar_quadro_memoria(self):
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

        self.value_end1 = tk.StringVar()
        self.label_value_end1 = tk.Label(self, textvariable=self.value_end1)
        self.value_end2 = tk.StringVar()
        self.label_value_end2 = tk.Label(self, textvariable=self.value_end2)
        self.value_end3 = tk.StringVar()
        self.label_value_end3 = tk.Label(self, textvariable=self.value_end3)
        self.value_end4 = tk.StringVar()
        self.label_value_end4 = tk.Label(self, textvariable=self.value_end4)
        self.label_mem_rec_usada.grid(row=6, column=8, columnspan=8, sticky="W")
        self.label_endereco.grid(row=7, column=8, columnspan=4, sticky="W")
        self.label_end1.grid(row=8, column=8, columnspan=4, sticky="E", padx=20)
        self.label_end2.grid(row=9, column=8, columnspan=4, sticky="E", padx=20)
        self.label_end3.grid(row=10, column=8, columnspan=4, sticky="E", padx=20)
        self.label_end4.grid(row=11, column=8, columnspan=4, sticky="E", padx=20)
        self.label_valor.grid(row=7, column=12, columnspan=4, sticky="W")
        self.label_value_end1.grid(row=8, column=12, columnspan=4, sticky="E", padx=20)
        self.label_value_end2.grid(row=9, column=12, columnspan=4, sticky="E", padx=20)
        self.label_value_end3.grid(row=10, column=12, columnspan=4, sticky="E", padx=20)
        self.label_value_end4.grid(row=11, column=12, columnspan=4, sticky="E", padx=20)

    def montar_informacoes_processador(self):
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
        self.label_clock.grid(row=12, column=8, columnspan=4, sticky="W")
        self.label_pc.grid(row=13, column=8, columnspan=4, sticky="W")
        self.label_inst_concluidas.grid(row=14, column=8, columnspan=4, sticky="W")
        self.label_produtividade.grid(row=15, column=8, columnspan=4, sticky="W")
        self.value_clock.grid(row=12, column=12, columnspan=4, sticky="E", padx=20)
        self.value_pc.grid(row=13, column=12, columnspan=4, sticky="E", padx=20)
        self.value_inst_concluidas.grid(row=14, column=12, columnspan=4, sticky="E", padx=20)
        self.value_produtividade.grid(row=15, column=12, columnspan=4, sticky="E", padx=20)

    def montar_registradores(self):
        # Registradores

        self.label_registradores = tk.Label(self, text="Registradores")
        self.label_registradores.grid(row=16, column=8, columnspan=8, sticky="W")
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
        self.label_r0.grid(row=17, column=8, sticky="W")
        self.label_r1.grid(row=18, column=8, sticky="W")
        self.label_r2.grid(row=19, column=8, sticky="W")
        self.label_r3.grid(row=20, column=8, sticky="W")
        self.label_r4.grid(row=21, column=8, sticky="W")
        self.label_r5.grid(row=22, column=8, sticky="W")
        self.label_r6.grid(row=23, column=8, sticky="W")
        self.label_r7.grid(row=24, column=8, sticky="W")
        self.label_r8.grid(row=17, column=10, sticky="W")
        self.label_r9.grid(row=18, column=10, sticky="W")
        self.label_r10.grid(row=19, column=10, sticky="W")
        self.label_r11.grid(row=20, column=10, sticky="W")
        self.label_r12.grid(row=21, column=10, sticky="W")
        self.label_r13.grid(row=22, column=10, sticky="W")
        self.label_r14.grid(row=23, column=10, sticky="W")
        self.label_r15.grid(row=24, column=10, sticky="W")
        self.label_r16.grid(row=17, column=12, sticky="W")
        self.label_r17.grid(row=18, column=12, sticky="W")
        self.label_r18.grid(row=19, column=12, sticky="W")
        self.label_r19.grid(row=20, column=12, sticky="W")
        self.label_r20.grid(row=21, column=12, sticky="W")
        self.label_r21.grid(row=22, column=12, sticky="W")
        self.label_r22.grid(row=23, column=12, sticky="W")
        self.label_r23.grid(row=24, column=12, sticky="W")
        self.label_r24.grid(row=17, column=14, sticky="W")
        self.label_r25.grid(row=18, column=14, sticky="W")
        self.label_r26.grid(row=19, column=14, sticky="W")
        self.label_r27.grid(row=20, column=14, sticky="W")
        self.label_r28.grid(row=21, column=14, sticky="W")
        self.label_r29.grid(row=22, column=14, sticky="W")
        self.label_r30.grid(row=23, column=14, sticky="W")
        self.label_r31.grid(row=24, column=14, sticky="W")
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
        self.value_r0.grid(row=17, column=9, sticky="E", padx=20)
        self.value_r1.grid(row=18, column=9, sticky="E", padx=20)
        self.value_r2.grid(row=19, column=9, sticky="E", padx=20)
        self.value_r3.grid(row=20, column=9, sticky="E", padx=20)
        self.value_r4.grid(row=21, column=9, sticky="E", padx=20)
        self.value_r5.grid(row=22, column=9, sticky="E", padx=20)
        self.value_r6.grid(row=23, column=9, sticky="E", padx=20)
        self.value_r7.grid(row=24, column=9, sticky="E", padx=20)
        self.value_r8.grid(row=17, column=11, sticky="E", padx=20)
        self.value_r9.grid(row=18, column=11, sticky="E", padx=20)
        self.value_r10.grid(row=19, column=11, sticky="E", padx=20)
        self.value_r11.grid(row=20, column=11, sticky="E", padx=20)
        self.value_r12.grid(row=21, column=11, sticky="E", padx=20)
        self.value_r13.grid(row=22, column=11, sticky="E", padx=20)
        self.value_r14.grid(row=23, column=11, sticky="E", padx=20)
        self.value_r15.grid(row=24, column=11, sticky="E", padx=20)
        self.value_r16.grid(row=17, column=13, sticky="E", padx=20)
        self.value_r17.grid(row=18, column=13, sticky="E", padx=20)
        self.value_r18.grid(row=19, column=13, sticky="E", padx=20)
        self.value_r19.grid(row=20, column=13, sticky="E", padx=20)
        self.value_r20.grid(row=21, column=13, sticky="E", padx=20)
        self.value_r21.grid(row=22, column=13, sticky="E", padx=20)
        self.value_r22.grid(row=23, column=13, sticky="E", padx=20)
        self.value_r23.grid(row=24, column=13, sticky="E", padx=20)
        self.value_r24.grid(row=17, column=15, sticky="E", padx=20)
        self.value_r25.grid(row=18, column=15, sticky="E", padx=20)
        self.value_r26.grid(row=19, column=15, sticky="E", padx=20)
        self.value_r27.grid(row=20, column=15, sticky="E", padx=20)
        self.value_r28.grid(row=21, column=15, sticky="E", padx=20)
        self.value_r29.grid(row=22, column=15, sticky="E", padx=20)
        self.value_r30.grid(row=23, column=15, sticky="E", padx=20)
        self.value_r31.grid(row=24, column=15, sticky="E", padx=20)

    def run_one_clock(self):
        self.controller.run_one_clock()

        # t = Thread(target=self.controller.run_one_clock)
        # t.start()
        # t.join()

        # Pausando através do "time", apenas para testar

    def run_clocks_continuously(self):

        self.controller.run_clocks_continuously()

    def pause(self):

        self.controller.pause()

    def update_interface(self):

        self.set_instrucoes()
        self.set_sinais_controle()
        self.set_memoria_rec_usada()
        self.set_informacoes_processador()
        self.set_registradores()

    def set_instrucoes(self):

        pipeline_instructions = self.controller.get_pipeline_phases_current_instruction()

        self.instrucao_if.set(pipeline_instructions[0])
        self.instrucao_di_rf.set(pipeline_instructions[1])
        self.instrucao_ex.set(pipeline_instructions[2])
        self.instrucao_mem.set(pipeline_instructions[3])
        self.instrucao_wb.set(pipeline_instructions[4])

    def set_sinais_controle(self):

        self.reg_dst.set("mudar!")
        self.alu_op1.set("mudar!")
        self.alu_op2.set("mudar!")
        self.alu_src.set("mudar!")
        self.branch.set("mudar!")
        self.mem_read.set("mudar!")
        self.mem_write.set("mudar!")
        self.reg_write.set("mudar!")
        self.mem_to_reg.set("mudar!")

    def set_memoria_rec_usada(self):

        self.end1.set("mudar valor!")
        self.end2.set("mudar valor!")
        self.end3.set("mudar valor!")
        self.end4.set("mudar valor!")
        self.value_end1.set("mudar valor!")
        self.value_end2.set("mudar valor!")
        self.value_end3.set("mudar valor!")
        self.value_end4.set("mudar valor!")

    def set_informacoes_processador(self):

        self.clock.set("mudar valor!")
        self.pc.set("mudar valor!")
        self.inst_concluidas.set("mudar valor!")
        self.produtividade.set("mudar valor!")

    def set_registradores(self):

        pipeline_registers = self.controller.get_pipeline_registers_value()

        self.r0.set(pipeline_registers[0])
        self.r1.set(pipeline_registers[1])
        self.r2.set(pipeline_registers[2])
        self.r3.set(pipeline_registers[3])
        self.r4.set(pipeline_registers[4])
        self.r5.set(pipeline_registers[5])
        self.r6.set(pipeline_registers[6])
        self.r7.set(pipeline_registers[7])
        self.r8.set(pipeline_registers[8])
        self.r9.set(pipeline_registers[9])
        self.r10.set(pipeline_registers[10])
        self.r11.set(pipeline_registers[11])
        self.r12.set(pipeline_registers[12])
        self.r13.set(pipeline_registers[13])
        self.r14.set(pipeline_registers[14])
        self.r15.set(pipeline_registers[15])
        self.r16.set(pipeline_registers[16])
        self.r17.set(pipeline_registers[17])
        self.r18.set(pipeline_registers[18])
        self.r19.set(pipeline_registers[19])
        self.r20.set(pipeline_registers[20])
        self.r21.set(pipeline_registers[21])
        self.r22.set(pipeline_registers[22])
        self.r23.set(pipeline_registers[23])
        self.r24.set(pipeline_registers[24])
        self.r25.set(pipeline_registers[25])
        self.r26.set(pipeline_registers[26])
        self.r27.set(pipeline_registers[27])
        self.r28.set(pipeline_registers[28])
        self.r29.set(pipeline_registers[29])
        self.r30.set(pipeline_registers[30])
        self.r31.set(pipeline_registers[31])


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

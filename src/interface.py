# coding: utf-8
import Tkinter as tk
import tkFileDialog
import tkMessageBox
from program_controller import ProgramController
from loader import Loader


class Interface(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("MIPS Simulator")
        self.file_loaded = False

        self.init_ui()

    def init_ui(self):

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
            width=10,
            command=self.open_file)
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
        
        self.label_r = []
        for register_number in range(32):
            register_name = "R" + str(register_number)
            self.label_r.append(tk.Label(self, text=register_name))

        row = 17
        column = 8
        for register_number in range(32):
            if row == 25:
                row = 17
                column += 2
            self.label_r[register_number].grid(
                row=row, column=column, sticky="W")
            row += 1

        self.r = []
        for register_number in range(32):
            self.r.append(tk.StringVar())

        self.value_r = []
        for register_number in range(32):
            self.value_r.append(tk.Label(
                self,
                textvariable=self.r[register_number]))
        
        row = 17
        column = 9
        for register_number in range(32):
            if row == 25:
                row = 17
                column += 2
            self.value_r[register_number].grid(
                row=row, column=column, sticky="E", padx=20)
            row += 1

    def run_one_clock(self):
        if self.file_loaded:
            self.controller.run_one_clock()

        # t = Thread(target=self.controller.run_one_clock)
        # t.start()
        # t.join()

        # Pausando através do "time", apenas para testar

    def run_clocks_continuously(self):

        if self.file_loaded:
            self.controller.run_clocks_continuously()

    def pause(self):

        if self.file_loaded:
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

        # TODO: tem que implementar o ALUOp1, ALUOp2, MemRead

        control_signals = self.controller.get_pipeline_phases_control_signals()

        reg_dst = control_signals[0].get('RegDst', '')
        alu_op1 = control_signals[0].get('ALUOp1', '')
        alu_op2 = control_signals[0].get('ALUOp2', '')
        alu_src = control_signals[0].get('ALUSrc', '')
        self.reg_dst.set(reg_dst)
        self.alu_op1.set(alu_op1)
        self.alu_op2.set(alu_op2)
        self.alu_src.set(alu_src)

        branch = control_signals[1].get('Branch', '')
        mem_read = control_signals[1].get('MemRead', '')
        mem_write = control_signals[1].get('MemWrite', '')
        self.branch.set(branch)
        self.mem_read.set(mem_read)
        self.mem_write.set(mem_write)

        reg_write = control_signals[2].get('RegWrite', '')
        mem_to_reg = control_signals[2].get('MemtoReg', '')
        self.reg_write.set(reg_write)
        self.mem_to_reg.set(mem_to_reg)

    def set_memoria_rec_usada(self):

        rec_mem = self.controller.get_recent_memory()

        self.end1.set(rec_mem[0][0])
        self.end2.set(rec_mem[1][0])
        self.end3.set(rec_mem[2][0])
        self.end4.set(rec_mem[3][0])
        self.value_end1.set(rec_mem[0][1])
        self.value_end2.set(rec_mem[1][1])
        self.value_end3.set(rec_mem[2][1])
        self.value_end4.set(rec_mem[3][1])

    def set_informacoes_processador(self):

        info = self.controller.get_information()

        self.clock.set(info['clock_number'])
        self.pc.set(info['pc'])
        self.inst_concluidas.set(info['finished_instructions'])
        self.produtividade.set(info['productivity'])

    def set_registradores(self):

        pipeline_registers = self.controller.get_pipeline_registers_value()

        for register_number in range(32):
            self.r[register_number].set(pipeline_registers[register_number])

    def open_file(self):
        try:
            filename = tkFileDialog.askopenfilename()
            l = Loader(filename)
            l.read_mem_values()
            self.controller = ProgramController()
            self.controller.interface = self
            self.controller.pipeline.mem = l.get_mem_x()
            self.controller.pipeline.mem.extend(l.get_mem_y())
            self.controller.pipeline.PC = l.get_pc()
            self.file_loaded = True
        except:
            tkMessageBox.showerror('Error', 'Não foi possível abrir o arquivo. Escolha outro')



def main():
    interface = Interface()
    interface.mainloop()


if __name__ == '__main__':
    main()

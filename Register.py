class Register():
    
    def __init__(self):
        self.value=0
        self.next_write_use = {"last_instruction_to_write": None,
                                  "waiting_write": False}
   
    def write(self, value, instruction):
        self.value=value
        if next_write_use["last_instruction_to_write"]==instruction:
            next_write_use["waiting_write": False]

class Register():
    
    def __init__(self):
        value=0
        next_write_use = {"last_instruction_to_write": None,
                          "waiting_write": False}

        def write(new_value, instruction):
            value = new_value
            if next_write_use["last_instruction_to_write"]==instruction:
                next_write_use["waiting_write"] = False
                
        def use():
            return value
        
        self.write = write
        self.get_value = use

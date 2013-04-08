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
        
        def is_waiting_for_use():
            return next_write_use["waiting_write"]
        
        def declare_last_write_use(instruction):
            next_write_use = {"last_instruction_to_write": instruction,
                                "waiting_write": True}
        
        self.write = write
        self.get_value = use
        self.is_waiting_for_use = is_waiting_for_use
        self.declare_last_write_use = declare_last_write_use

class Register():

    def __init__(self):
        value = {1: 0}
        next_write_use = {"last_instruction_to_write": None,
                          "waiting_write": False}

        def write(new_value, instruction):
            if not isinstance(new_value, int):
                raise TypeError("type of value is not an integer")
            value[1] = new_value
            if next_write_use["last_instruction_to_write"] == instruction:
                next_write_use["waiting_write"] = False

        def use():
            return value[1]

        def is_waiting_for_use():
            return next_write_use["waiting_write"]

        def next_instruction_to_write():
            return next_write_use['last_instruction_to_write']

        def declare_last_write_use(instruction):
            next_write_use["last_instruction_to_write"] = instruction
            next_write_use["waiting_write"] = True

        def concede_right_to_use(instruction):
            if next_write_use["last_instruction_to_write"] == instruction:
                next_write_use["waiting_write"] = False

        self.write = write
        self.get_value = use
        self.is_waiting_for_use = is_waiting_for_use
        self.next_instruction_to_write = next_instruction_to_write
        self.declare_last_write_use = declare_last_write_use
        self.concede_right_to_use = concede_right_to_use
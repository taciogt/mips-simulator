# coding: utf-8

class ProgramController(object):
	def run_clock(self):
		pass
	
	def run_entire_program(self):
		pass
	
	def pause(self):
	    pass
	    
	def openFile(self):
	    pass
	
	#Contains the last four adresses used in memory
    recently_used_mem = [0, 0, 0, 0]
	
	#deletes the oldest memory from our list and adds
	#a new one. This is used by the GUI to know which 
	#were the last 4 used memory adresses and to get their
	#values (so that they can be shown)
	def add_used_mem(self, mem_address):
	    del recently_used_mem[0]
	    recently_used.append(mem_address)
	
    clock_number = 0
    finished_instructions = 0
    
    def get_productivity(self):
        return finished_instructions/clock_number

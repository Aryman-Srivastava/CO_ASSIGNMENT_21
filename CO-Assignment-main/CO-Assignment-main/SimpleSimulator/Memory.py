# Mem
import RegisterFile as RF 

class Memory:
	
	def __init__(self):
		self.mem_data = {}
		self.inst_dict = {}
		IF = open("InstructionFile.txt", 'r')
		lineno = 0
		for line in IF.readlines():
			self.inst_dict[lineno] = line  
		IF.close()

	def get_var(self, var):
		return self.mem_data[var]
	def set_mem(self, reg_val, var):	# same as update()
		self.mem_data[var] = reg_val

	def fetch(self, PC, cycle):
		return self.inst_dict[PC]

	def dump(self):
		for key in self.mem_data.keys():
			print(self.mem_data[key])


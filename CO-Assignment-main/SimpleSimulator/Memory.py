# Mem
import matplotlib.pyplot as plt

class Memory:
	
	def __init__(self):
		self.mem_dict = {}
		self.x = []
		self.y = []
		for i in range(256):
			self.mem_dict[i] = "0000000000000000"
		IF = open("InstructionFile.txt", 'r+')
		lineno = 0
		for line in IF.readlines():
			self.mem_dict[lineno] = line  
			lineno += 1
		IF.close()

	def get_var(self, var):
		return self.mem_dict[var]

	def set_mem(self, reg_val, var):	# same as update()
		self.mem_dict[var] = (bin(reg_val)[2:]).rjust(16, '0')

	def fetch(self, PC, cycle):
        	if self.mem_dict[PC][:5] in ['00100', '00101']:
            		# self.y.append([PC, int(self.mem_dict[PC][8:16], 2)])
            		self.x.append(cycle)
            		self.x.append(cycle)
            		self.y.append(PC)
            		self.y.append(int(self.mem_dict[PC][8:16], 2))
        	else:
            		self.y.append(PC)
            		self.x.append(cycle)
        	return self.mem_dict[PC]

	def dump(self):
		for i in range(256):
			if '\n' in self.mem_dict[i]:
				print(self.mem_dict[i][:-1])
			else:
				print(self.mem_dict[i])

	def show_traces(self):
		plt.scatter(self.x, self.y)
		plt.savefig('pattern.png')

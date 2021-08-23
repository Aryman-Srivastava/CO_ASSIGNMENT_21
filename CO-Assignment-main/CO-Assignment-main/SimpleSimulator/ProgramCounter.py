# PC
class ProgramCounter:
	
	def __init__(self):
		self.pc = 0
	def getVal(self):
		return self.pc
	def update(self, next_pc):
		self.pc = next_pc
	def dump(self):
		pc_val = bin(self.pc-1)[2:] 
		print(pc_val.rjust(8, '0'), end=" ")
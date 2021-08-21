# Execution Engine
import RegisterFile as RF
import Memory as Mem
import ProgramCounter as pc

class ExecutionEngine:
 
	# self.rf and rf will have different values
	# suggestion: make dump() in ExecutionEngine 

	def __init__(self, rf, mem, PC):
		self.rf = rf
		self.mem = mem
		self.PC = pc
		self.halted = False
		self.next_pc = 0

	def execute(self, inst, cycle):
		inst_type = self.rf.get_inst_type(inst)
		if inst_type in ["A", "B", "C", "D"]:
			self.rf.update(inst)
			self.PC.update(self.PC.getVal() + 1)
		elif inst_type == "E":
			if inst[:5] == "01111":
				self.next_pc = int(inst[8:16], 2)
				self.PC.update(self.next_pc)
			elif inst[:5] == "10000":
				L_flag = int(self.rf.getFLAGS()[-3], 2)
				if L_flag == 1:
					self.next_pc = int(inst[8:16], 2)
					self.PC.update(self.next_pc)
				else:
					self.PC.update(self.PC.getVal() + 1)
			elif inst[:5] == "10001":
				G_flag = int(self.rf.getFLAGS()[-2], 2)
				if G_flag == 1:
					self.next_pc = int(inst[8:16], 2)
					self.PC.update(self.next_pc)
				else:
					self.PC.update(self.PC.getVal() + 1)
			elif inst[:5] == "10010":
				E_flag = int(self.rf.getFLAGS()[-1], 2)
				if E_flag == 1:
					self.next_pc = int(inst[8:16], 2)
					self.PC.update(self.next_pc)
				else:
					self.PC.update(self.PC.getVal() + 1)
		elif inst_type == "F":
			self.halted = True
		
		return self.halted, self.next_pc 


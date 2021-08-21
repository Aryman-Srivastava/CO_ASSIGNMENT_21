# register_file
# REMIND A CHANGE := reg_val --> self.reg_val

import instruction as ins
import Memory as mem

reg_addr = {
	"000": "R0", "001": "R1", "010": "R2", "011": "R3", "100": "R4", "101": "R6", "110": "R6", "111": "FLAGS"
}

# FLAGS --> 000000000000VLGE

memory = mem.Memory()

class RegisterFile:

	def __init__(self):
		self.reg_val = {
			"R0" : 0, "R1" : 0, "R2" : 0, "R3" : 0, "R4" : 0, "R5" : 0, "R6" : 0, "FLAGS" : "0000000000000000"
		}
	def getFLAGS(self):
		return self.reg_val["FLAGS"]

	def get_inst_type(self, inst):
		if inst in ["add", "sub", "mul", "xor", "or", "and"]:
			return "A"
		elif inst in ["mov_Imm", "rs", "ls"]:
			return "B"
		elif inst in ["mov_reg", "div", "not", "cmp"]:
			return "C"
		elif inst in ["ld", "st"]:
			return "D"
		elif inst in ["jmp", "jlt", "jgt", "je"]:
			return "E"
		elif inst == "hlt":
			return "F"

	def update(self, inst):
		inst_op = ins.op_codes[inst[:5]]
		inst_type = get_inst_type(inst_op)

		if inst_type == "A":
			reg_1 = inst[7:10]
			reg_2 = inst[10:13]
			reg_3 = inst[13:16]

			if inst_op == "add":
				self.reg_val[reg_addr[reg_1]] = self.reg_val[reg_addr[reg_2]] + self.reg_val[reg_addr[reg_3]]
				if self.reg_val[reg_addr[reg_1]] > 65535:
					self.reg_val[reg_addr[reg_1]] = int(bin(self.reg_val[reg_addr[reg_1]])[-16:], 2)
					self.reg_val["FLAGS"] = "0000000000001000"

			elif inst_op == "sub":
				self.reg_val[reg_addr[reg_1]] = self.reg_val[reg_addr[reg_2]] - self.reg_val[reg_addr[reg_3]]
				if self.reg_val[reg_addr[reg_1]] < 0:
					self.reg_val[reg_addr[reg_1]] = 0
					self.reg_val["FLAGS"] = "0000000000001000"

			elif inst_op == "mul":
				self.reg_val[reg_addr[reg_1]] = self.reg_val[reg_addr[reg_2]] * self.reg_val[reg_addr[reg_3]]
				if self.reg_val[reg_addr[reg_1]] > 65535:
					self.reg_val[reg_addr[reg_1]] = int(bin(self.reg_val[reg_addr[reg_1]])[-16:], 2)
					self.reg_val["FLAGS"] = "0000000000001000"

			elif inst_op == "xor":
				self.reg_val[reg_addr[reg_1]] = self.reg_val[reg_addr[reg_2]] ^ self.reg_val[reg_addr[reg_3]]

			elif inst_op == "or":
				self.reg_val[reg_addr[reg_1]] = self.reg_val[reg_addr[reg_2]] | self.reg_val[reg_addr[reg_3]]

			elif inst_op == "and":
				self.reg_val[reg_addr[reg_1]] = self.reg_val[reg_addr[reg_2]] & self.reg_val[reg_addr[reg_3]]
		
		elif inst_type == "B":
			reg = inst[5:8]
			imm_val = int(inst[8:16], 2)

			if inst_op == "mov_Imm":
				self.reg_val[reg_addr[reg]] = imm_val

			elif inst_op == "ls":
				shift_val = self.reg_val[reg_addr[reg]] << imm_val
				self.reg_val[reg_addr[reg]] = shift_val
			elif inst_op == "rs":
				self.reg_val[reg_addr[reg]] = self.reg_val[reg_addr[reg]] >> imm_val

		elif inst_type == "C":
			reg_1 = inst[10:13]
			reg_2 = inst[13:16]

			if inst_op == "mov_reg":
				self.reg_val[reg_addr[reg_1]] = self.reg_val[reg_addr[reg_2]]
			elif inst_op == "div":
				# Division by zero to be handled?
				self.reg_val["R0"] = self.reg_val[reg_addr[reg_1]] // self.reg_val[reg_addr[reg_2]]
				self.reg_val["R1"] = self.reg_val[reg_addr[reg_1]] % self.reg_val[reg_addr[reg_2]]
			elif inst_op == "not":
				self.reg_val[reg_addr[reg_1]] = ~ self.reg_val[reg_addr[reg_2]]
			elif inst_op == "cmp":
				if self.reg_val[reg_addr[reg_1]] < self.reg_val[reg_addr[reg_2]]:
					self.reg_val["FLAGS"] = "0000000000000100"
				elif self.reg_val[reg_addr[reg_1]] > self.reg_val[reg_addr[reg_2]]:
					self.reg_val["FLAGS"] = "0000000000000010"
				elif self.reg_val[reg_addr[reg_1]] == self.reg_val[reg_addr[reg_2]]:
					self.reg_val["FLAGS"] = "0000000000000001" 	

		elif inst_type == "D":
			reg = inst[5:8]
			var = inst[8:16]

			if inst_op == "ld":
				self.reg_val[reg_addr[reg]] = memory.get_var(var)	# get_var(var) --> gets the address of var 
																# from memory
			elif inst_op == "st":
				memory.set_mem(self.reg_val[reg_addr[reg]], var)	# set_mem(register_value, var) --> stores the value in
															# given register into the memory pointed at by var
	
	def dump(self):
		for reg in self.reg_val.keys():
			if reg != "FLAGS":
				print(bin(self.reg_val[reg])[2:])
			else:
				print(self.reg_val["FLAGS"])
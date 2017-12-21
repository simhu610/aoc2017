import operator

class Instruction():
    def __init__(self, line):
        x = line.split()
        assert len(x) == 7
        assert x[3] == "if"
        self.reg_change = x[0]
        self.incdec = x[1]
        self.value_change = int(x[2])
        self.reg_cond = x[4]
        self.op_cond = x[5]
        self.value_cond = int(x[6])

lines = open("8").readlines()

registers = {}
vals = []

for line in lines:
    instruction = Instruction(line)
    if instruction.reg_cond in registers:
        reg_value_cond = registers[instruction.reg_cond]
    else:
        reg_value_cond = 0
    if eval("{}{}{}".format(reg_value_cond, instruction.op_cond, instruction.value_cond)):
        if instruction.reg_change not in registers:
            registers[instruction.reg_change] = 0
        ops = {"inc": operator.add, "dec": operator.sub}
        registers[instruction.reg_change] = ops[instruction.incdec](registers[instruction.reg_change], instruction.value_change)
        vals.append(registers[instruction.reg_change])

print max([registers[r] for r in registers])
print max(vals)
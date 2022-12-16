
with open("input",'r') as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###
class CPU:
    def __init__(self,instructions:list[str]):
        self.X = 1
        self.clock = 0
        self.instructions = instructions
        self.registerSum = 0
        self.run()

    @staticmethod
    def parse_instruction(instruction:str) -> int:
        inst_type = instruction.split(" ")[0]
        return 1 if inst_type == "noop" else 2 if inst_type == "addx" else None

    def run(self):
        for idx,inst in enumerate(self.instructions):
            timer = self.parse_instruction(inst)
            for j in range(timer):
                self.clock += 1
                if (self.clock + 20) % 40 ==0 and self.X:
                    self.registerSum += self.clock * self.X
                if j==timer-1 and inst.split(" ")[0] == "addx":
                    self.X += int(inst.split(" ")[-1])

cpu = CPU(data)
print(f"### Part 1 ###\nRegister sum: {cpu.registerSum}") # >7020

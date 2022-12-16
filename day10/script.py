
with open("input",'r') as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###
class CPU:
    def __init__(self,instructions:list[str]):
        self.X = 1
        self.clock = 0
        # inst_timer keeps track of the number of clock cycles left until instruction is executed
        #self.inst_timer:dict[str,int] = {}
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
            #if timer is None:
            #    raise ValueError(f"Invalid instruction: {inst}")
            for j in range(timer):
                self.clock += 1
                if (self.clock + 20) % 40 ==0 and self.X:
                    self.registerSum += self.clock * self.X
                if j==timer-1 and inst.split(" ")[0] == "addx":
                    self.X += int(inst.split(" ")[-1])
                

#data ="""addx 15
#addx -11
#addx 6
#addx -3
#addx 5
#addx -1
#addx -8
#addx 13
#addx 4
#noop
#addx -1
#addx 5
#addx -1
#addx 5
#addx -1
#addx 5
#addx -1
#addx 5
#addx -1
#addx -35
#addx 1
#addx 24
#addx -19
#addx 1
#addx 16
#addx -11
#noop
#noop
#addx 21
#addx -15
#noop
#noop
#addx -3
#addx 9
#addx 1
#addx -3
#addx 8
#addx 1
#addx 5
#noop
#noop
#noop
#noop
#noop
#addx -36
#noop
#addx 1
#addx 7
#noop
#noop
#noop
#addx 2
#addx 6
#noop
#noop
#noop
#noop
#noop
#addx 1
#noop
#noop
#addx 7
#addx 1
#noop
#addx -13
#addx 13
#addx 7
#noop
#addx 1
#addx -33
#noop
#noop
#noop
#addx 2
#noop
#noop
#noop
#addx 8
#noop
#addx -1
#addx 2
#addx 1
#noop
#addx 17
#addx -9
#addx 1
#addx 1
#addx -3
#addx 11
#noop
#noop
#addx 1
#noop
#addx 1
#noop
#noop
#addx -13
#addx -19
#addx 1
#addx 3
#addx 26
#addx -30
#addx 12
#addx -1
#addx 3
#addx 1
#noop
#noop
#noop
#addx -9
#addx 18
#addx 1
#addx 2
#noop
#noop
#addx 9
#noop
#noop
#noop
#addx -1
#addx 2
#addx -37
#addx 1
#addx 3
#noop
#addx 15
#addx -21
#addx 22
#addx -6
#addx 1
#noop
#addx 2
#addx 1
#noop
#addx -10
#noop
#noop
#addx 20
#addx 1
#addx 2
#addx 2
#addx -6
#addx -11
#noop
#noop
#noop""".split("\n")
cpu = CPU(data)
print(f"### Part 1 ###\nRegister sum: {cpu.registerSum}") # >7020

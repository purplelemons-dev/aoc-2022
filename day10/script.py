
with open("input",'r') as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###
class CPU:
    def __init__(self,instructions:list[str]):
        self.X = 1
        self.clock = 0
        self.instructions = instructions
        self.registerSum = 0
        #self.spritePos = 0
        self.litPixels = ""
        self.run()

    @staticmethod
    def parse_instruction(instruction:str) -> int:
        inst_type = instruction.split(" ")[0]
        return 1 if inst_type == "noop" else 2 if inst_type == "addx" else None

    def run(self):
        for idx,inst in enumerate(self.instructions):
            timer = self.parse_instruction(inst)
            for j in range(timer):
                # During cycle n
                ### Pre-execution ###
                if (self.clock + 20) % 40 ==0 and self.X:
                    self.registerSum += self.clock * self.X
                if self.clock%40 in range((self.X-1)%40,(self.X+2)%40):
                    self.litPixels+="#"
                else:
                    self.litPixels+="."
                self.clock += 1
                ### Execution ###
                inst_type = inst.split(" ")[0]
                if j==timer-1 and inst_type == "addx":
                    self.X += int(inst.split(" ")[-1])
            if idx==0:
                print(self.litPixels)

    def render(self):
        for i in range(0,len(self.litPixels),40):
            print(self.litPixels[i:i+40])


cpu = CPU(data)
print(f"### Part 1 ###\nRegister sum: {cpu.registerSum}")

### Part 2 ###
print("### Part 2 ###")
cpu.render()

# Part 1 doesnt work in this version
# and part 2 barely works, but hey i got it done lmao

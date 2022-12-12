
with open("input",'r') as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###
class CPU:
    def __init__(self,instructions:list[str]):
        self.X = 1
        self.clock = 0
        # inst_timer keeps track of the number of clock cycles left until instruction is executed
        self.inst_timer:dict[str,int] = {}
        self.instructions = instructions
    
    def execute(self):
        for inst in self.inst_timer:
            if self.inst_timer[inst] == 0:
                # Execute instruction
                if inst == "noop": pass
                elif inst.startswith("addv "):
                    v = int(inst.split(" ")[1])
                    self.X += v
                else:
                    raise Exception("Unknown instruction: " + inst)
                # Reset instruction timer
                del self.inst_timer[inst]
            else:
                self.inst_timer[inst] -= 1

    def cycle(self):
        


with open("input",'r') as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###

class Monkey:
    def __init__(self,lines:list[str]):
        self.times_inspected = 0
        self.id:int = int(lines[0].split(" ")[-1][:-1])
        self.current_items = [int(i) for i in lines[1].split("Starting items: ")[-1].split(", ")]
        opstring = lines[2].split("new = ")[-1].split(" ")
        a = opstring[0]
        b = opstring[2]
        operator = opstring[1]
        self.evalOperator = self.createEvalOperator(a,b,operator)
        self.moduloCheck = self.createModuloCheck(int(lines[3].split(" by ")[-1]))
        self.onTrue = int(lines[4].split(" ")[-1])
        self.onFalse = int(lines[5].split(" ")[-1])

    @staticmethod
    def createEvalOperator(a:str,b:str,operator:str):
        a,b=int(a) if a.isnumeric() else None,int(b) if b.isnumeric() else None
        if operator == "+":
            if a is None and b is None: return lambda x,y: x+y
            elif a is None: return lambda x: b+x
            elif b is None: return lambda x: a+x
            else: raise ValueError("Expected at least one unknown variable")
        elif operator == "*":
            if a is None and b is None: return lambda x: x*x
            elif a is None: return lambda x: b*x
            elif b is None: return lambda x: a*x
            else: raise ValueError("Expected at least one unknown variable")
        else: raise ArithmeticError(f"Invalid operator: {operator}")
    
    @staticmethod
    def createModuloCheck(modulo:int):
        return lambda x: x%modulo == 0

monkies:list[Monkey] = []

for idx,line in enumerate(data[::7]):
    idx*=7
    monkies.append(Monkey(data[idx:idx+7]))

for round in range(20):
    for m in monkies:
        for idx,item in enumerate(m.current_items.copy()):
            item = m.evalOperator(item)//3
            m.current_items.pop(0)
            m.times_inspected += 1
            monkies[m.onTrue if m.moduloCheck(item) else m.onFalse].current_items.append(item)

final="\n".join(f"{m_id}: {m.times_inspected}" for m_id,m in enumerate(monkies))
print(f"### Part 1 ###\n{final}")

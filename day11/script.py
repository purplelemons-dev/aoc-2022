
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
        self.modulo = int(lines[3].split(" by ")[-1])
        self.moduloCheck = self.createModuloCheck()
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

    def createModuloCheck(self):
        return lambda x: x%self.modulo==0

monkeys:list[Monkey] = []

for idx,line in enumerate(data[::7]):
    idx*=7
    monkeys.append(Monkey(data[idx:idx+7]))

for round in range(20):
    for m in monkeys:
        for item in m.current_items.copy():
            item = m.evalOperator(item)//3
            m.current_items.pop(0)
            m.times_inspected += 1
            monkeys[m.onTrue if m.moduloCheck(item) else m.onFalse].current_items.append(item)

final = [m.times_inspected for m in monkeys]
max1 = max(final)
final.remove(max1)
max2 = max(final)
print(f"### Part 1 ###\n{max1*max2}")

### Part 2 ###

MOD=1
for m in monkeys: MOD *= m.modulo

class Monkey2:
    def __init__(self,items:list[int],operation_line:str,modulo:int,onTrue:int,onFalse:int):
        self.times_inspected = 0
        self.current_items = items
        operator = "+" if "+" in operation_line else "*"
        self.operation_line = operation_line
        try:
            op_int = int(operation_line.split(f"{operator} ")[-1])
            self.operation = lambda x: eval(f"{x}{operator}{op_int}")
        except ValueError: self.operation = lambda x: eval(f"{x}{operator}{x}")
        self.modulo = modulo
        self.onTrue = onTrue
        self.onFalse = onFalse

monkeys:list[Monkey2]=[]
for idx,line in enumerate(data[::7]):
    idx*=7
    items = [int(i) for i in data[idx+1].strip("Starting items: ").split(", ")]
    operation_line = data[idx+2].strip("Operation: new = old ")
    modulo = int(data[idx+3].strip("Test: divisible by "))
    onTrue = int(data[idx+4].strip("If true: throw to monkey "))
    onFalse = int(data[idx+5].strip("If false: throw to monkey "))
    
    monkeys.append(Monkey2(items,operation_line,modulo,onTrue,onFalse))

for round in range(10**4):
    for idx,m in enumerate(monkeys):
        #print(f"Round {round+1} - Monkey {idx+1} - {m.current_items}")
        m.times_inspected += len(m.current_items)
        for item in m.current_items:
            item = m.operation(item) % MOD
            monkeys[
                m.onTrue if not item%m.modulo
                else m.onFalse
            ].current_items.append(item)
        m.current_items=[]

final = [m.times_inspected for m in monkeys]
max1 = max(final)
final.remove(max1)
max2 = max(final)

print(f"### Part 2 ###\n{max1*max2}") # <1477464551264

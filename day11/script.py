
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

monkies:list[Monkey] = []

for idx,line in enumerate(data[::7]):
    idx*=7
    monkies.append(Monkey(data[idx:idx+7]))

for round in range(20):
    for m in monkies:
        for item in m.current_items.copy():
            item = m.evalOperator(item)//3
            m.current_items.pop(0)
            m.times_inspected += 1
            monkies[m.onTrue if m.moduloCheck(item) else m.onFalse].current_items.append(item)

final = [m.times_inspected for m in monkies]
max1 = max(final)
final.remove(max1)
max2 = max(final)
print(f"### Part 1 ###\n{max1*max2}")

### Part 2 ###

monkies:list[Monkey] = []

data="""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".split("\n")

for idx,line in enumerate(data[::7]):
    idx*=7
    monkies.append(Monkey(data[idx:idx+7]))

for round in range(10**5):
    for m in monkies:
        #print(f"Round {round} - Monkey {m.id} - {m.current_items}")
        for item in m.current_items.copy():
            item = m.evalOperator(item) % m.modulo
            m.current_items.pop(0)
            m.times_inspected += 1
            monkies[m.onTrue if m.moduloCheck(item) else m.onFalse].current_items.append(item)

final = [m.times_inspected for m in monkies]
max1 = max(final)
final.remove(max1)
max2 = max(final)

#* 2713310158
#  266747029810
#  271412780082

print(f"### Part 2 ###\n{max1*max2}") # <1477464551264

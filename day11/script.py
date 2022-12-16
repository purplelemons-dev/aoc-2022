
with open("input",'r') as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###

def evalOperator(a,b,operator):
    if operator == "+": return a+b
    elif operator == "*": return a*b
    elif operator == "-": return a-b
    else: raise ArithmeticError(f"Invalid operator: {operator}")

class Monkey:
    def __init__(self,lines:list[str]):
        self.inspected_items = []
        self.id:int = int(lines[0].split(" ")[-1][:-1])
        self.starting_iems = [int(i) for i in lines[1].split("Starting items: ")[-1].split(", ")]
        self.operation = "+" if "+" in lines[2] else "*" if "*" in lines[2] else "-" if "-" in lines[2] else None




with open("input", "r") as f: data = [x.strip() for x in f.readlines()]

overlaps=0

def parse(elf:str)->tuple[int,int]: return tuple(map(int,elf.split("-")))

### Part 1 ###

for line in data:
    elf1, elf2 = line.split(",")
    elf1x, elf1y = parse(elf1)
    elf2x, elf2y = parse(elf2)
    if set(range(elf1x,elf1y+1)).issubset(range(elf2x,elf2y+1)) or set(range(elf2x,elf2y+1)).issubset(range(elf1x,elf1y+1)): overlaps+=1

print(f"### Part 1 ###\n{overlaps= }")

### Part 2 ###

overlaps=0

for line in data:
    elf1, elf2 = line.split(",")
    elf1x, elf1y = parse(elf1)
    elf2x, elf2y = parse(elf2)
    if elf1x <= elf2x <= elf1y or elf2x <= elf1x <= elf2y: overlaps+=1

print(f"### Part 2 ###\n{overlaps= }")


with open("input",'r') as f: data = [x for x in f.readlines()]

### Part 1 ###

initial = data[:8]
instructions = [x.strip() for x in data[10:]]

def parse_initial_cargo(initial:list[str])->dict[int,list[str]]:
    cargo = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
    for i in initial:
        for j in cargo:
            char = i[j*4+1]
            if char!=" ": cargo[j].append(char)
    for i in cargo: cargo[i] = cargo[i][::-1]
    return cargo

cargo = parse_initial_cargo(initial)
for i in instructions:
    move = int(i.split(" ")[1])
    from_ = int(i.split(" ")[3])-1
    to = int(i.split(" ")[5])-1
    cargo[to]+=[cargo[from_].pop() for i in range(move)]

print(f"### Part 1 ###\nMessage: {''.join(i[-1] for i in cargo.values())}")

### Part 2 ###
cargo = parse_initial_cargo(initial)
for i in instructions:
    move = int(i.split(" ")[1])
    from_ = int(i.split(" ")[3])-1
    to = int(i.split(" ")[5])-1
    cargo[to]+=[cargo[from_].pop() for i in range(move)][::-1]

print(f"### Part 2 ###\nMessage: {''.join(i[-1] for i in cargo.values())}")

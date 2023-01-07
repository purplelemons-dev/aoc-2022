
with open("input") as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###
structure:set[complex] = set()

for line in data:
    vertices = line.split(" -> ")
    for idx,pair in enumerate(vertices[:-1]):
        x1,y1 = map(int,pair.split(","))
        x2,y2 = map(int,vertices[idx+1].split(","))
        if x1 == x2:
            for y in range(min(y1,y2),max(y1,y2)+1):
                structure.add(complex(x1,y))
        elif y1 == y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                structure.add(complex(x,y1))
copied=structure.copy()
part2=structure.copy()

def get_next_pos(pos:complex, structure:set[complex])->complex:
    if pos+1j not in structure:
        return pos+1j
    elif pos-1+1j not in structure:
        return pos-1+1j
    elif pos+1+1j not in structure:
        return pos+1+1j
    else:
        return None

def print_structure(structure:set[complex]):
    min_x,max_x,min_y,max_y = min(structure,key=lambda x: x.real).real,max(structure,key=lambda x: x.real).real,min(structure,key=lambda x: x.imag).imag,max(structure,key=lambda x: x.imag).imag
    print("*"*10)
    for y in range(int(min_y),int(max_y)+1):
        for x in range(int(min_x),int(max_x)+1):
            if complex(x,y) in structure:
                if complex(x,y) in copied:
                    print("#",end="")
                else:
                    print(".",end="")
            else:
                print(" ",end="")
        print()

sand,current,high_pos=0,complex(500,0),max(structure,key=lambda x: x.imag).imag
try:
    while 1:
        new_pos = get_next_pos(current,structure)
        if current.imag >= high_pos:
            break
        elif new_pos is None:
            sand += 1
            structure.add(current)
            current = complex(500,0)
        else:
            current = new_pos
except KeyboardInterrupt:
    print(sand)

print(f"### Part 1 ###\n{sand= }")

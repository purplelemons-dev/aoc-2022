
with open("input",'r') as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###

map=list(list(x) for x in data)
moves:set[complex]=set()
nodes:list[complex]=[]
current=end=0j

def translate(x:str):
    if x.islower(): return ord(x)-97
    elif x=="S": return 0
    elif x=="E": return 25
    else: raise ValueError("Invalid input")

for y,line in enumerate(map):
    for x,point in enumerate(line):
        if point=="S": current=complex(x,y)
        elif point=="E": end=complex(x,y)

def allowed_moves(pos:complex,moves_taken:set[complex]):
    x,y=round(pos.real),round(pos.imag)
    a_moves:set[complex]=set()
    pos_value = translate(map[y][x])
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        if x+dx in range(len(map[0])) and y+dy in range(len(map)):
            if dx+dy*1j in moves_taken: continue
            new_value = translate(map[y+dy][x+dx])
            if new_value<=pos_value+1:
                a_moves.add(complex(x+dx,y+dy))
    return a_moves

while True:
    moves.add(nodes[-1])
    options = allowed_moves(nodes[-1],moves)
    if len(options)>1:
        nodes.append(current)
        ...
    elif len(options)==1:
        nodes[-1]=current
    elif len(options)==0:
        ...

print(solve(set(),current))

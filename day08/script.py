
with open("input",'r') as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###

# Transform data
a=[]
for line in data: a.append(list(map(int,[i for i in line])))

def neighbors(x:int, y:int) -> dict[str,int]:
    """Returns a dictionary of the neighbors of a pixel"""
    init={
        "U": None,
        "D": None,
        "L": None,
        "R": None,
    }
    for i,j in ((0,-1),(-1,0),(0,1),(1,0)):
        try:
            if ij: pass # TODO fix what huh
            init["URDL"[i+j]] = a[x+i][y+j]
        except IndexError:
            pass
    return init


with open("input",'r') as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###
striiing = [x for x in data[0]]

def lmaooo():
    for idx,_ in enumerate(striiing):
        if len(set(striiing[idx:idx+4])) == 4: return idx+4

print(f"### Part 1 ###\n{lmaooo()= }")

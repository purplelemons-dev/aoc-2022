
with open("input", 'r') as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###

prioritySum = 0

def priority(x:str):
    # Lowercase (a-z): 1-26
    # Uppercase (A-Z): 27-52
    return (ord(x) - 64)+26 if x.isupper() else ord(x) - 96

def findCommonChar(a:str, b:str):
    for i in a:
        if i in b: return i

for i in data:
    half = len(i) // 2
    sack1, sack2 = i[:half], i[half:]

    prioritySum += priority(findCommonChar(sack1, sack2))

print(f"### Part 1 ###\n{prioritySum= }")

### Part 2 ###

badgeSum=0

def findCommonChar(a:str, b:str, c:str):
    for i in a:
        if i in b and i in c: return i

for idx,sack in enumerate(data[::3]):
    idx=idx*3
    sack1, sack2, sack3 = data[idx:idx+3]

    badgeSum+=priority(findCommonChar(sack1,sack2,sack3))

print(f"### Part 2 ###\n{badgeSum= }")

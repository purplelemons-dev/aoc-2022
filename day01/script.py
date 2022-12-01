
with open("input",'r') as f:
    data = f.read().splitlines()


### Part 1 ###
elves={}
elf=0
for i in data:
    if i=='': elf+=1
    else:
        try:elves[elf]+=int(i)
        except:elves[elf]=int(i)

print(max(elves.values()))

### Part 2 ###

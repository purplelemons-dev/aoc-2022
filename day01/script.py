
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

print("Part 1: "+str(max(elves.values())))

### Part 2 ###

#swapped={j:i for i,j in elves.items()}
calories=list(elves.values())
calories.sort()
print(f"Part 2: {sum(calories[-3:])}")

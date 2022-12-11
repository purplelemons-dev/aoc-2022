
with open("input",'r') as f: data = [x.strip() for x in f.readlines()]
#data="""00000
#33333
#22222
#33333
#44244""".split("\n")

### Part 1 ###

def transpose(array:list[list])->list[list]:
    return list(map(list,zip(*array)))

# Transform data
array=[]
key=[]
for line in data: array.append([int(x) for x in line])
#print(f"{len(array)= }")
#print(f"{len(array[0])= }")
transposed = transpose(array)

for i,row in enumerate(array):
    current=[]
    if i%100==0: print(f"{row= }")
    for j,cell in enumerate(row):
        #print(f"{(i,j)= }")
        if 0<i<len(array)-1 and 0<j<len(row)-1:
            current.append(
                all([
                    # Match with left side
                    cell>x for x in row[:j]
                ])
                or
                all([
                    # Match with right side
                    cell>x for x in row[j+1:]
                ])
                or
                all([
                    # Match with upper column
                    cell>x for x in transposed[j][:i]
                ])
                or
                all([
                    # Match with lower column
                    cell>x for x in transposed[j][i+1:]
                ])
            )
        else:
            current.append(True)
    key.append(current)

treesVisible = sum([sum(x) for x in key])
print(f"### Part 1 ###\n{treesVisible= }")

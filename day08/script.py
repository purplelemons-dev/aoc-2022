
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
transposed = transpose(array)

for i,row in enumerate(array):
    current=[]
    for j,cell in enumerate(row):
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

### Part 2 ###
keys2=[]

for i,row in enumerate(array):
    subtotal=[]
    for j,cell in enumerate(row):
        if 0<i<len(array)-1 and 0<j<len(row)-1:
            # \/ stupidest piece of code i've ever written \/
            up,down,left,right = 0,0,0,0
            # Left
            current = row[:j][::-1]
            for x in current:
                left+=1
                if x>=cell: break
            # Right
            current = row[j+1:]
            for x in current:
                right+=1
                if x>=cell: break
            # Up
            current = transposed[j][:i][::-1]
            for x in current:
                up+=1
                if x>=cell: break
            # Down
            current = transposed[j][i+1:]
            for x in current:
                down+=1
                if x>=cell: break
            subtotal.append(up*down*left*right)
        else: continue
    keys2.append(subtotal)

total=[]
for i in keys2:
    # problems with empty lists for some reason dont ask me why
    if i: total.append(max(i))
print(f"### Part 2 ###\n{max(total)= }")

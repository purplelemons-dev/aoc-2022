
from json import loads
from functools import cmp_to_key

with open("input") as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###

pairs:list[tuple['list|int']]=[]
for idx, line in enumerate(data[::3]):
    idx*=3
    pairs.append((loads(line),loads(data[idx+1])))

def right_order(left:'int|list', right:'int|list',debug:bool=False):
    type_left, type_right = type(left), type(right)
    if left == right: return None
    if type_left == type_right == int:
        return left < right
    elif type_left != type_right:
        if type_left == int: return right_order([left], right, debug)
        elif type_right == int: return right_order(left, [right], debug)
    assert type_left == type_right == list
    for l, r in zip(left, right):
        order = right_order(l, r, debug)
        if debug: print(f"  {l} < {r} = {order}")
        if order is not None: return order
    return len(left) < len(right)

indexsum=0
for idx, (left, right) in enumerate(pairs):
    idx+=1
    order_check = right_order(left, right)
    if order_check: indexsum+=idx
print(f"### Part 1 ###\n{indexsum}")

### Part 2 ###
packets,answer=[loads(line) for line in data if line],[]
packets+=[[[2]],[[6]]]
def new_order(left:'int|list', right:'int|list',debug:bool=False):
    if right_order(left, right, debug): return -1
    elif right_order(right, left, debug): return 1
    return 0
packets = sorted(packets,key=cmp_to_key(new_order))
for idx,packet in enumerate(packets):
    if packet in ([[6]],[[2]]): answer+=[idx+1]
print(f"### Part 2 ###\n{answer[0]*answer[1]}")

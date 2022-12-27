
from json import loads

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

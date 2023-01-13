
with open("input") as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###

Y=2000000
lim=4000000
if 1:
    data="""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split("\n")
    Y=10
    lim=20

sensors:dict[complex,int]={}
blocked:set[complex]=set()
for line in data:
    sensor_x = int(line.split("Sensor at x=")[1].split(", ")[0])
    sensor_y = int(line.split("y=")[1].split(":")[0])
    beacon_x = int(line.split("is at x=")[1].split(",")[0])
    beacon_y = int(line.split("is at x=")[1].split("=")[1])
    sensors[complex(sensor_x, sensor_y)] = abs(beacon_x-sensor_x)+abs(beacon_y-sensor_y)

for sensor in sensors:
    s=sensors[sensor]
    y=int(sensor.imag)
    d=abs(y-Y)
    if not d<=s: continue
    l=2*abs(s-d)+1
    start_x, end_x = int(sensor.real)-l//2, int(sensor.real)+l//2
    blocked.update(complex(x,Y) for x in range(start_x, end_x+1))

answer = len(blocked) - 1 # I dont know why I need to subtract 1
if not answer < 4560026:
    raise ArithmeticError(f"Answer ({answer}) out of bounds")
print(f"### Part 1 ###\n{answer= }")

### Part 2 ###
del blocked
grid:dict[int,set[range]]={}

def tuning_freq(coord:complex):
    return 4000000*int(coord.real) + int(coord.imag)

def get_surrounding(center:complex,size:int) -> dict[int,range]:
    """Returns a dictionary of y-values corresponding to a range of x values that the object occupies"""
    y_ranges:dict[int,range]={}
    x_center,y_center=int(center.real), int(center.imag)
    for y in range(y_center-size, y_center+size+1):
        d=abs(y-y_center)
        l=2*abs(size-d)+1
        start_x, end_x = x_center-l//2, x_center+l//2
        y_ranges[y] = range(start_x, end_x+1)
    return y_ranges

for sensor in sensors:
    # TODO: fix the way that the grid is handled
    for y,new_range in get_surrounding(sensor,sensors[sensor]).items():
        working=True
        if y<0: continue
        try:
            print(f"{y= }")
            # TODO CHANGE INTO A (recursive) FUNC
            while working and any(xr.start<new_range.start<xr.stop or xr.start<new_range.stop<xr.stop for xr in grid[y]):
                for xr in grid[y].copy():
                    print(grid[y])
                    if xr.start<new_range.start<xr.stop or xr.start<new_range.stop<xr.stop:
                        print(f"merging {xr} {new_range}")
                        grid[y].remove(xr)
                        grid[y].add(range(min(xr.start,new_range.start),max(xr.stop,new_range.stop)))
                        working=False
                        break

            #for xr in grid[y].copy():
            #    if xr.start<=new_range.start<=xr.stop or xr.start<=new_range.stop<=xr.stop:
            #        grid[y].remove(xr)
            #        grid[y].add(range(min(xr.start,new_range.start),max(xr.stop,new_range.stop)))
            #        break
        except KeyError:
            grid[y]={new_range}

print("done generating grid")
#exit()
def main():
    for y in grid:
        for x in range(0,lim+1):
            if all(x not in xr for xr in grid[y]):
                answer = tuning_freq(complex(x,y))
                #if not answer > 2503905: raise ArithmeticError(f"Answer ({answer}) out of bounds")
                print(f"### Part 2 ###\n{x,y= }\n{answer= }")
                return
    else:
        raise Exception("No answer found")
main()

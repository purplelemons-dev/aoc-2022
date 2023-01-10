
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
def tuning_freq(coord:complex):
    return lim*int(coord.real) + int(coord.imag)

def a(coord:complex):
    return all(map(lambda i: 0<=i<=lim, (coord.real, coord.imag)))

def get_surrounding(coord:complex,size:int):
    # Iterate through the y values (coord.imag-size -> coord.imag+size)
    # Iterate through the x values between the derrived points on the current y value (coord.real-l//2 -> coord.real+l//2)
    for y in range(int(coord.imag)-size, int(coord.imag)+size+1):
        d=abs(y-int(coord.imag))
        l=2*abs(size-d)+1
        start_x, end_x = int(coord.real)-l//2, int(coord.real)+l//2
        for x in range(start_x, end_x+1):
            yield complex(x,y)

def main():
    for y in range(0,lim+1):
        for x in range(0,lim+1):
            coord = complex(x,y)
            if coord in blocked or not a(coord): continue
            print(f"### Part 2 ###\n{tuning_freq(coord)= }")
            return
    else:
        raise ArithmeticError(f"Answer ({answer}) out of bounds")
main()

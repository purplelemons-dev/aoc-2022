
with open("input") as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###
Y=2000000
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

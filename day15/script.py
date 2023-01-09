
with open("input") as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###
#sensors:set[complex] = set()
#beacons:set[complex] = set()
#grid:set[complex] = set() 
#for line in data:
#    sensor_x = int(line.split("Sensor at x=")[1].split(", ")[0])
#    sensor_y = int(line.split("y=")[1].split(":")[0])
#    beacon_x = int(line.split("is at x=")[1].split(",")[0])
#    beacon_y = int(line.split("is at x=")[1].split("=")[1])
#
#    sensors.add(complex(sensor_x, sensor_y))
#    beacons.add(complex(beacon_x, beacon_y))
#
#def get_adj(pos:complex):
#    return {pos + i for i in (-1, 1, -1j, 1j)}
#
#for sensor in sensors:
#    current,itr = {sensor}, 0
#    while 1:
#        if current & beacons:
#            pass # intersection
#        else:
#            itr+=1
#            for pos in current:
#                # Add all adjacent positions to current
#                #  that are not already in current
#                current|=get_adj(pos)^current

sensors:dict[complex,int]={}
for line in data:
    sensor_x = int(line.split("Sensor at x=")[1].split(", ")[0])
    sensor_y = int(line.split("y=")[1].split(":")[0])
    beacon_x = int(line.split("is at x=")[1].split(",")[0])
    beacon_y = int(line.split("is at x=")[1].split("=")[1])
    sensors[complex(sensor_x, sensor_y)] = abs(beacon_x-sensor_x)+abs(beacon_y-sensor_y)

def get_occupies(sensor:complex,dist:int,at_y:int=2000000):#->set[complex]:
    occupied_spaces=int(2*abs(dist-(sensor.imag-at_y))+1)
    out:set[complex]=set()
    mid:complex=sensor-at_y*1j if sensor.imag>at_y else sensor+at_y*1j
    for i in range(int(mid.real)-occupied_spaces//2,int(mid.real)+occupied_spaces//2+1):
        yield complex(i,at_y)#out.add(complex(i,at_y))
    #return out

coord=1872170+78941j
print(len(tuple(get_occupies(coord, sensors[coord]))))

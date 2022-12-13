
with open("input",'r') as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###

class RopeTrail:

    def __init__(self):
        self.head_pos:complex = 0j
        self.tail_pos:complex = 0j
        self.tail_visited:set[complex] = set()

    @property
    def near(self):
        return (
            abs(self.head_pos.real-self.tail_pos.real)<=1
            and abs(self.head_pos.imag-self.tail_pos.imag)<=1
        )

    @property
    def unique_visits(self):
        return len(self.tail_visited)

    def translate(self, direction:str):
        try:
            return {
                "U": 0+1j,
                "D": 0-1j,
                "L": -1+0j,
                "R": 1+0j
            }[direction]
        except KeyError: raise ValueError("Invalid direction")


    def move(self, direction:str):
        offset = self.translate(direction)
        self.head_pos += offset
        if not self.near:
            if offset.imag == 0:
                self.tail_pos = self.head_pos - offset.real
            elif offset.real == 0:
                self.tail_pos = self.head_pos - offset.imag*1j
            else: raise ValueError("Invalid offset")
            self.tail_visited.add(self.tail_pos)

trail = RopeTrail()
for line in data:
    direction, distance = line.split(" ")
    for _ in range(int(distance)):
        trail.move(direction)

print(f"### Part 1 ###\n{trail.unique_visits= }")

### Part 2 ###
class NewRopeTrail:
    def __init__(self):
        self.trails = [0j]*10
        self.tail_visited = set()
    
    @staticmethod
    def near(pos1:complex, pos2:complex):
        return (
            abs(pos1.real-pos2.real)<=1
            and abs(pos1.imag-pos2.imag)<=1
        )

    @property
    def unique_visits(self):
        return len(self.tail_visited)

    @staticmethod
    def translate(direction:str):
        try:
            return {
                "U": 0+1j,
                "D": 0-1j,
                "L": -1+0j,
                "R": 1+0j
            }[direction]
        except KeyError: raise ValueError("Invalid direction")
    
    def move(self, direction:str):
        offset = self.translate(direction)
        self.trails[0] += offset
        for idx, trail in enumerate(self.trails[1:]):
            idx+=1
            if self.near(trail, self.trails[idx-1]):
                break
            else:
                pos1 = trail
                self.trails[idx] = self.trails[idx-1] + offset
                offset = trail - pos1
        self.tail_visited.add(self.trails[-1])

trail = NewRopeTrail()
for line in data:
    direction, distance = line.split(" ")
    for _ in range(int(distance)):
        trail.move(direction)

print(f"### Part 2 ###\n{trail.unique_visits= }")

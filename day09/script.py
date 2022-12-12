
with open("input",'r') as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###

class RopeTrail:

    def __init__(self):
        self.head_pos:complex = 0+0j
        self.tail_pos:complex = 0+0j
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

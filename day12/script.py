
with open("input",'r') as f: data=f.read() #data = [x.strip() for x in f.readlines()]

### Part 1 ###

from a_star import coord
import a_star

class node(a_star.node):

    def neighbors(self, map: dict[coord, 'node'], dim: tuple[int, int]):
        x, y = self.pos
        dim_x, dim_y = dim
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            if x+dx in range(dim_x) and y+dy in range(dim_y):
                _node = map[coord(x+dx,y+dy)]
                if self.numvalue >= _node.numvalue-1:
                    yield _node

    def update(self,map:dict[coord,'node'],dim:tuple[int,int]):
        temp=set()
        for neighbor in self.neighbors(map,dim):
            if neighbor.discovered and not (self.numvalue > neighbor.numvalue+1):
                temp.add(neighbor)
            else:
                yield neighbor
        self.parent = min(temp,key=lambda i:i.distance) if temp else None
        self.distance=self.parent.distance+1 if self.parent else 0

    @property
    def numvalue(self)->int:
        if self.value==self.value.lower():
            return ord(self.value)-97
        elif self.value=="S":
            return 0
        elif self.value=="E":
            return 25
        else:
            raise ValueError("Invalid cell value")

class pathfinder:
    def __init__(self,textmap:str):
        self.textmap=textmap
        self.map:dict[coord,node]={
            coord(x,y):node(coord(x,y),cell)
                for y,line in enumerate(textmap.splitlines())
                    for x,cell in enumerate(line)
        }
        self.dimensions=(len(textmap.splitlines()),len(textmap.splitlines()[0]))[::-1]
        for _node in self.map.values():
            if _node.value=="S": self.current={_node}
            elif _node.value=="E": self.end=_node

    def run(self):
        while 1:
            next_nodes:set[node]=set()
            for _node in self.current:
                next_nodes.update(_node.update(self.map,self.dimensions))
            if self.end.discovered:
                return self.end.distance
            self.current=next_nodes
        
    @property
    def solved(self):
        current=self.end
        temp=[list(i) for i in self.textmap.splitlines()]
        while 1:
            if current.value=="S": return "\n".join("".join(i) for i in temp)
            current=current.parent
            print(current)
            pos_x, pos_y = current.pos
            temp[pos_y][pos_x]="."

given_map = data

path = pathfinder(given_map)
print(path.run())
print(path.solved)

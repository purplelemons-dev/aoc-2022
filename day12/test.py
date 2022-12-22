
class coord(complex):
    @property
    def x(self):
        return round(self.real)
    @property
    def y(self):
        return round(self.imag)
    def __iter__(self):
        return iter((self.x,self.y))


given_map="""
#S#######
# # #  E#
#       #
# # #   #
#       #
#########"""[1:]

class node:
    def __eq__(self, __o:'node') -> bool: return self.pos==__o.pos
    def __ne__(self, __o:'node') -> bool: return not self==__o
    def __hash__(self) -> int: return hash(self.pos)
    def __init__(self,pos:coord,value:str):
        self.pos=pos
        self.value=value
        self.distance=None

    @property
    def discovered(self):
        return True if isinstance(self.distance,int) else False

    def neighbors(self,map:dict[coord,'node'],dim:tuple[int,int]):
        x,y = self.pos
        dim_x,dim_y = dim
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            if x+dx in range(dim_x) and y+dy in range(dim_y):
                temp_node = map[coord(x+dx,y+dy)]
                if temp_node.value!="#":
                    yield temp_node

    def update(self,map:dict[coord,'node'],dim:tuple[int,int]):
        """Ensure that you do not update a wall node.
        This can be done by checking `node.value` before calling this method."""
        temp=set()
        for neighbor in self.neighbors(map,dim):
            if neighbor.discovered:
                temp.add(neighbor.distance)
            else:
                yield neighbor
        self.distance=min(temp)+1 if temp else 0


class pathfinder:
    def __init__(self,textmap:str):
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
            next_nodes=set()
            for _node in self.current:
                next_nodes.update(_node.update(self.map,self.dimensions))
            if self.end.discovered:
                return self.end.distance
            self.current=next_nodes

if __name__=="__main__":
    print(pathfinder(given_map).run())

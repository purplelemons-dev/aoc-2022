
with open("input",'r') as f: data = [x.strip() for x in f.readlines()]

### Part 1 ###

class File:
    def __init__(self, name:str, size:int):
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name:str, parent:'Directory'=None):
        self.name = name
        self.parent = parent
        self.children:list[Directory|File] = []
    
    @property
    def size(self):
        return sum([x.size for x in self.children])

root=Directory("/")
current=root
data.pop(0) # do this because we manually added the root directory
while True:
    try:
        line = data.pop(0)
    except IndexError: break
    if line.startswith("$ "):
        # this is a command
        if line.startswith("$ cd "):
            dirname = line[len("$ cd "):]
            if dirname=="..":
                current=current.parent
            else:
                for i in current.children:
                    if i.name==dirname and isinstance(i, Directory):
                        current=i
                        break
                else: raise Exception(f"Directory {dirname} not found")
        elif line=="$ ls":
            # list files
            temp:list[str]=[]
            for i in data:
                if i.startswith("$ "): break
                temp.append(i)
            for i in temp:
                data.pop(0)
                if i[0].isdigit():
                    size, name = i.split(" ")
                    obj=File(name, int(size))
                else: obj=Directory(i[len("dir "):], current)

                current.children.append(obj)

abcd = []
def pogchamp(directory:Directory):
    if directory.size <= 100000:
        abcd.append(directory.size)
    for i in directory.children:
        if isinstance(i, Directory):
            pogchamp(i)
pogchamp(root)
print(f"### Part 1 ###\n{sum(abcd)= }")

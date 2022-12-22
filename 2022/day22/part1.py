import re

def get_opp(loc, dir, map):
    if dir == 0:
        for i in range(0, loc[1]):
            if (loc[0], i) in map:
                return (loc[0], i)
    elif dir == 1:
        for i in range(0, loc[0]):
            if (i, loc[1]) in map:
                return (i, loc[1])
    elif dir == 2:
        for i in range(200, loc[1], -1):
            if (loc[0], i) in map:
                return (loc[0], i)
    elif dir == 3:
        for i in range(200, loc[0], -1):
            if (i, loc[1]) in map:
                return (i, loc[1])

def main():
    with open("test.txt") as f:
        content = f.read()
    
    dirs = {
        0: ">",
        1: "v",
        2: "<",
        3: "^",
    }
    inst = None
    loc = None
    dir = 0
    map = {}
    cont = content.split('\n')
    for i in range(len(cont)):
        if cont[i] == '':
            inst = re.split('(\d+)', cont[i+1])
            break
        else:
            for j in range(len(cont[i])):
                if cont[i][j] != " ":
                    if loc == None:
                        loc = (i,j)
                    map[(i,j)] = cont[i][j] 
    for i in inst:
        if i.isnumeric():
            for _ in range(int(i)):
                x, y = loc
                if dir == 0:
                    if (x, y+1) not in map:
                        loc = get_opp(loc, dir, map)
                    elif map[(x, y+1)] == '#':
                        break
                    else:
                        loc = (x, y+1)
                elif dir == 1:
                    if (x+1, y) not in map:
                        loc = get_opp(loc, dir, map)
                    elif map[(x+1, y)] == '#':
                        break
                    else:
                        loc = (x+1, y)
                elif dir == 2:
                    if (x, y-1) not in map:
                        loc = get_opp(loc, dir, map)
                    elif map[(x, y-1)] == '#':
                        break
                    else:
                        loc = (x, y-1)
                elif dir == 3:
                    if (x-1, y) not in map:
                        loc = get_opp(loc, dir, map)
                    elif map[(x-1, y)] == '#':
                        break
                    else:
                        loc = (x-1, y)
        elif i in {"R", "L"}:
            if i == "R":
                dir = (dir+1) % 4
            elif i == "L":
                dir = (dir-1) % 4
    print(f'row: {loc[0]+1}\ncol: {loc[1]+1}\ndir: {dirs[dir]}')
    print(1000*(loc[0]+1) + 4*(loc[1]+1) + dir)
if __name__ == "__main__":
    raise SystemExit(main())


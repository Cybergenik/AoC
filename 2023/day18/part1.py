#!/usr/local/bin/python3

def adj(x, y):
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)

def find_trench(start, inst):
    trench = set([start])
    curr = start
    for dir, n in inst:
        if dir == "R":
            for i in range(n):
                n = (curr[0], curr[1]+1)
                trench.add(n)
                curr = n
        elif dir == "L":
            for i in range(n):
                n = (curr[0], curr[1]-1)
                trench.add(n)
                curr = n
        elif dir == "D":
            for i in range(n):
                n = (curr[0]+1, curr[1])
                trench.add(n)
                curr = n
        elif dir == "U":
            for i in range(n):
                n = (curr[0]-1, curr[1])
                trench.add(n)
                curr = n
    return trench

def fill_trench(start, trench):
    work = [start]
    while work:
        v = work.pop()
        if v not in trench:
            trench.add(v)
            for u in adj(*v):
                work.append(u)
    return len(trench)

def print_map(trench, xdims, ydims):
    for x in range(xdims[0], xdims[1]):
        for y in range(ydims[0], ydims[1]):
            if (x,y) in trench:
                print("#", end="")
            else:   
                print(".", end="")
        print("")
    print("")

def find_dims(trench):
    Sx = 0
    Sy = 0
    Ex = 0
    Ey = 0
    for x, y in trench:
        if x < Sx:
            Sx = x
        if y < Sy:
            Sy = y
        if y > Ey:
            Ey = y
        if x > Ex:
            Ex = x
    return (Sx, Ex+1), (Sy, Ey+1)

def main():
    with open("input.txt") as f:
        content = f.readlines()

    instructions = []
    for l in content:
        dir, n, _ = l.strip().split()
        instructions.append((dir, int(n)))
    
    start = (0,0) 
    trench = find_trench(start, instructions)
    dims = find_dims(trench)
    print_map(trench, *dims)
    print(fill_trench((1,1), trench))

if __name__ == "__main__":
    raise SystemExit(main())

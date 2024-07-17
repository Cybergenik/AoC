#!/usr/local/bin/python3

from tqdm import tqdm

def find_trench(start, inst):
    trench = [start]
    curr = start
    for dir, n in tqdm(inst):
        if dir == 0:
            n = (curr[0], curr[1]+n)
            trench.append(n)
        elif dir == 1:
            n = (curr[0]+n, curr[1])
            trench.append(n)
        elif dir == 2:
            n = (curr[0], curr[1]-n)
            trench.append(n)
        elif dir == 3:
            n = (curr[0]-n, curr[1])
            trench.append(n)
        curr = n
    return trench

#https://en.wikipedia.org/wiki/Shoelace_formula
def area_poly(trench):
    area = 0
    for p1, p2 in zip(trench[:-1], trench[1:]):
        det = (p1[0] * p2[1]) - (p2[0] * p1[1])
        area += det
    area = abs(area) + 1
    for p1, p2 in zip(trench[:-1], trench[1:]):
        area += max(p1[0], p2[0]) - min(p1[0], p2[0])
        area += max(p1[1], p2[1]) - min(p1[1], p2[1])
    return area/2

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
        inst = l.strip().split("#")[-1][:-1]
        dir = int(inst[-1])
        n = int(inst[:-1], 16)
        instructions.append((dir, n))
    
    start = (0,0) 
    trench = find_trench(start, instructions)
    dims = find_dims(trench)
    print(dims)
    print(area_poly(trench))

if __name__ == "__main__":
    raise SystemExit(main())

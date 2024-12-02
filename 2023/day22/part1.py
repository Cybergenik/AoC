#!/usr/local/bin/python3

from collections import defaultdict
from tqdm import tqdm

def brick_set(xs, ys, zs):
    bricks = set()
    for x in range(xs[0], xs[1]+1):
        for y in range(ys[0], ys[1]+1):
            for z in range(zs[0], zs[1]+1):
                bricks.add((x, y, z))
    return bricks

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    bricks = []
    for l in content:
        b1, b2 = l.strip().split("~")
        x1, y1, z1 = map(int, b1.split(","))
        x2, y2, z2 = map(int, b2.split(","))
        bricks.append([(x1, x2), (y1, y2), (z1, z2)])

    bricks = sorted(bricks, key=lambda x: min(x[2]))
    deps = defaultdict(set)
    prev_max_z = 0
    for i, b in tqdm(enumerate(bricks)):
        diff = (prev_max_z - b[2][0]) + 1
        b[2] = (b[2][0]+diff, b[2][1]+diff)
        while min(b[2]) > 1:
            hit = False
            falling_brick = brick_set(*b)
            for j in range(i):
                # One of these is a dead loop
                mbrick = max(bricks[j][2])
                ground_brick = brick_set(bricks[j][0], bricks[j][1], (mbrick+1,
                                                                      mbrick+1))
                if len(falling_brick & ground_brick) > 0:
                    hit = True
                    deps[i].add(j)
            if hit:
                break
            b[2] = (b[2][0]-1, b[2][1]-1)
        prev_max_z = max(prev_max_z, b[2][1])

    unremovable_set = set()
    for b1, b_set in deps.items():
        if len(b_set) < 2:
            unremovable_set |= b_set

    print(len(bricks)-len(unremovable_set))       

if __name__ == "__main__":
    raise SystemExit(main())

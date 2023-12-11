#!/usr/local/bin/python3

from tqdm import tqdm
from collections import defaultdict

def adj(x, y, N, M):
    #North
    if x > 0:
        yield (x-1, y)
    #South
    if x < N:
        yield (x+1, y)
    #East
    if y > 0:
        yield (x, y-1)
    #West
    if y < M:
        yield (x, y+1)

def shortest_paths(start, ends, sys, exp_row, exp_col, N, M):
    work = [(start, 0)]
    seen = set()
    found = 0
    dists = 0
    while work:
        v = work.pop(0)
        if v[0] not in seen:
            if v[0] in ends:
                #print(f'{start} -> {v[0]}: {v[1]}')
                dists += v[1]
                found += 1
                if found == len(ends):
                    return dists
            seen.add(v[0])
            for u in adj(*v[0], N, M):
                added = 1
                if u[0] in exp_row:
                    added += 1
                if u[1] in exp_col:
                    added += 1
                work.append((u, v[1]+added))
    return 0

def main():
    with open("input.txt") as f:
        content = f.readlines()

    system = defaultdict(lambda: ".")
    exp_row = set()
    exp_col = set()
    N = len(content)
    M = len(content[0].strip())
    gal = set()
    for x, l in enumerate(content):
        l = l.strip()
        if "#" not in l:
            exp_row.add(x)
        for y, c in enumerate(l):
            system[(x,y)] = c
            if c == "#":
                gal.add((x,y))

    for y in range(len(content[0].strip())):
        if "#" not in "".join(system[(x, y)] for x in range(len(content))):
            exp_col.add(y)

    total = 0
    for g in tqdm(list(gal)):
        #print(f'Galaxy {g}:')
        gal.remove(g)
        total += shortest_paths(g, gal, system, exp_row, exp_col, N, M)
    print(total)
            
if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/local/bin/python3

from collections import defaultdict
#from collections import Counter

def sim(robots, secs, N, M):
    locs = robots[:]
    for _ in range(secs):
        for i, ((rx,ry), (rdx, rdy)) in enumerate(locs):
            nx, ny = (rx+rdx)%N, (ry+rdy)%M
            locs[i] = ((nx, ny), (rdx, rdy))
    return [x[0] for x in locs]

def print_board(locs, N, M):
    for ny in range(M):
        for nx in range(N):
            if (nx, ny) in locs:
                print(locs.count((nx,ny)), end=" ")
            else:
                print(".", end=" ")
        print("")
    print("")

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    robots = []
    for l in content:
        l, r = l.strip().split(" ")
        x, y = l[2:].split(",")
        vx, vy = r[2:].split(",")
        robots.append( ( (int(x),int(y)), (int(vx),int(vy)) ) )
    
    N = 101
    M = 103
    quads = [0,0,0,0]
    locs = sim(robots, 100, N, M)
    for loc in locs:
        if loc[0] < N//2:
            if loc[1] < M//2:
                quads[0] += 1
            if loc[1] > M//2:
                quads[1] += 1
        elif loc[0] > N//2:
            if loc[1] < M//2:
                quads[2] += 1
            elif loc[1] > M//2:
                quads[3] += 1
    print(quads)
    total = quads[0]
    for q in quads[1:]: total *= q
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

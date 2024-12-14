#!/usr/local/bin/python3

from collections import defaultdict
#from collections import Counter

def sim(robots, secs, N, M):
    locs = robots[:]
    for s in range(secs):
        for i, ((rx,ry), (rdx, rdy)) in enumerate(locs):
            nx, ny = (rx+rdx)%N, (ry+rdy)%M
            locs[i] = ((nx, ny), (rdx, rdy))

        qs = calculate_quads([x[0] for x in locs], N, M)
        for q, qq in zip(qs[:-1],qs[1:]):
            if abs(q - qq) > 200:
                print_board([x[0] for x in locs], N, M)
                return s+1

def print_board(locs, N, M):
    for ny in range(M):
        for nx in range(N):
            if (nx, ny) in locs:
                print(locs.count((nx,ny)), end=" ")
            else:
                print(".", end=" ")
        print("")
    print("")

def calculate_quads(robots, N, M):
    quads = [0,0,0,0]
    for loc in robots:
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
    return quads

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
    min_secs = sim(robots, 1000000, N, M)
    print(min_secs)

if __name__ == "__main__":
    raise SystemExit(main())

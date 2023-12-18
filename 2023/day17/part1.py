#!/usr/local/bin/python3

# (position, direction, tempo, dist)
def adj(loc, N, M):
    x, y = loc[0]
    dir = loc[1]
    tempo = loc[2]
    if dir == "u":
        #left
        if y > 0:
            yield ((x, y-1), "l", 1)
        #right
        if y < M-1:
            yield ((x, y+1), "r", 1)
        #straight
        if tempo < 3:
            if x > 0:
                yield ((x-1, y), "u", tempo+1)
    elif dir == "d":
        #left
        if y > 0:
            yield ((x, y-1), "l", 1)
        #right
        if y < M-1:
            yield ((x, y+1), "r", 1)
        #straight
        if tempo < 3:
            if x < N-1:
                yield ((x+1, y), "d", tempo+1)
    elif dir == "l":
        #up
        if x > 0:
            yield ((x-1, y), "u", 1)
        #down
        if x < N-1:
            yield ((x+1, y), "d", 1)
        #straight
        if tempo < 3:
            if y > 0:
                yield ((x, y-1), "l", tempo+1)
    elif dir == "r":
        #up
        if x > 0:
            yield ((x-1, y), "u", 1)
        #down
        if x < N-1:
            yield ((x+1, y), "d", 1)
        #straight
        if tempo < 3:
            if y < M-1:
                yield ((x, y+1), "r", tempo+1)

# (position, direction, tempo, dist)
def shortest_path(start, map, N, M):
    s = (start, "r", 1, 0)
    min_heat = 999999999999999999999
    work = [s]
    seen = set()
    while work:
        v = work.pop()
        if v not in seen:
            seen.add(v)
            if v[0] == (N-1, M-1):
                min_heat = min(min_heat, v[3])
                continue
            for u in adj(v, N, M):
                if v[3]+map[u[0]] < min_heat:
                    uu = (*u, v[3]+map[u[0]])
                    work.append(uu)
    return min_heat

def main():
    with open("test.txt") as f:
        content = f.readlines()

    N = len(content)
    M = len(content[0].strip())
    m = {}
    for x, l in enumerate(content):
        l = l.strip()
        for y, c in enumerate(l):
            m[(x, y)] = int(c)
    
    start = (0,0) 
    print(shortest_path(start, m, N, M))

if __name__ == "__main__":
    raise SystemExit(main())

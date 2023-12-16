#!/usr/local/bin/python3

from collections import defaultdict

def adj(v, N, M, m):
    x, y = v[0]
    if v[1] == "u":
        if m[(x, y)] == "-":
            if y > 0:
                yield ((x, y-1), "l")
            if y < M-1:
                yield ((x, y+1), "r")
        elif m[(x, y)] == "/":
            if y < M-1:
                yield ((x, y+1), "r")
        elif m[(x, y)] == "\\":
            if y > 0:
                yield ((x, y-1), "l")
        elif x > 0 :
            yield ((x-1, y), "u")
    elif v[1] == "d":
        if m[(x, y)] == "-":
            if y > 0:
                yield ((x, y-1), "l")
            if y < M-1:
                yield ((x, y+1), "r")
        elif m[(x, y)] == "/":
            if y > 0:
                yield ((x, y-1), "l")
        elif m[(x, y)] == "\\":
            if y < M-1:
                yield ((x, y+1), "r")
        elif x < N-1:
            yield ((x+1, y), "d")
    elif v[1] == "r":
        if m[(x, y)] == "|":
            if x > 0 :
                yield ((x-1, y), "u")
            if x < N-1:
                yield ((x+1, y), "d")
        elif m[(x, y)] == "/":
            if x > 0 :
                yield ((x-1, y), "u")
        elif m[(x, y)] == "\\":
            if x < N-1:
                yield ((x+1, y), "d")
        elif y < M-1:
            yield ((x, y+1), "r")
    elif v[1] == "l":
        if m[(x, y)] == "|":
            if x > 0 :
                yield ((x-1, y), "u")
            if x < N-1:
                yield ((x+1, y), "d")
        elif m[(x, y)] == "/":
            if x < N-1:
                yield ((x+1, y), "d")
        elif m[(x, y)] == "\\":
            if x > 0 :
                yield ((x-1, y), "u")
        elif y > 0:
            yield ((x, y-1), "l")

def track_beam(start, m, N, M):
    work = [(start, "r")]
    seen = set()
    while work:
        v = work.pop()
        if v not in seen:
            seen.add(v)
            for u in adj(v, N, M, m):
                work.append(u)

    return {v[0] for v in seen}

def print_seen(map, N, M, seen):
    for x in range(N):
        for y in range(M):
            if (x, y) in seen:
                print("#", end="")
            else:
                print(map[(x,y)], end="")
        print("")
    print("")

def main():
    with open("input.txt") as f:
        content = f.readlines()
    N = len(content)
    M = len(content[0].strip())
    m = defaultdict(lambda: "")
    for x, l in enumerate(content):
        l = l.strip()
        for y, c in enumerate(l):
            m[(x, y)] = c
    
    start = (0,0) 
    mirrs = track_beam(start, m, N, M) 
    #print_seen(m, N, M, mirrs)
    print(len(mirrs))

if __name__ == "__main__":
    raise SystemExit(main())

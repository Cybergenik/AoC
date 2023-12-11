#!/usr/local/bin/python3

from collections import defaultdict

def adj(x, y, graph):
    #North
    if graph[(x-1, y)] in "|F7":
        yield (x-1, y)
    #South
    if graph[(x+1, y)] in "|LJ":
        yield (x+1, y)
    #East
    if graph[(x, y-1)] in "-LF":
        yield (x, y-1)
    #West
    if graph[(x, y+1)] in "-J7":
        yield (x, y+1)

def find_loop(start: tuple[int, int], pipes):
    work = [start]
    seen = set()
    while work:
        v = work.pop()
        if v not in seen:
            seen.add(v)
            for u in adj(*v, pipes):
                work.append(u)
    return seen

def fill_loop(loop, pipes, N, M):
    total = 0
    for x in range(N):
        inside = False
        prev = None
        y = 0
        print(f"\nLine {x}")
        while y < M:
            curr = (x, y)
            #print(curr, inside)
            if curr in loop:
                print(pipes[curr], end=" ")
                if pipes[curr] in "|":
                    inside = not inside
                elif pipes[curr] in "LF":
                    prev = pipes[curr]
                else:
                    if (prev == "F" and pipes[curr] == "J") \
                    or (prev == "L" and pipes[curr] == "7"):
                        inside = not inside
                        prev = None
                print(int(inside), end=" ")
            if inside and curr not in loop:
                print(f'Inside: {curr}')
                total += 1
            y += 1
    return total

def main():
    with open("test2.txt") as f:
        content = f.readlines()
        
    pipes = defaultdict(lambda: "X")
    start = None
    N = len(content)
    M = len(content[0].strip())
    for x, l in enumerate(content):
        l = l.strip()
        for y, c in enumerate(l):
            pipes[(x, y)] = c
            if c == "S":
                start = (x, y)

    pipes[start] = "7"
    loop = find_loop(start, pipes)
    print(fill_loop(loop, pipes, N, M))

if __name__ == "__main__":
    raise SystemExit(main())

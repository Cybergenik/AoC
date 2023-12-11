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
    work = [(start, 0)]
    seen = set()
    largest = 0
    while work:
        v = work.pop(0)
        if v[0] not in seen:
            if v[1] > largest:
                largest = v[1]
            seen.add(v[0])
            for u in adj(*v[0], pipes):
                work.append((u, v[1]+1))
    return largest

def main():
    with open("input.txt") as f:
        content = f.readlines()
        
    pipes = defaultdict(lambda: "X")
    start = None
    for x, l in enumerate(content):
        l = l.strip()
        for y, c in enumerate(l):
            pipes[(x, y)] = c
            if c == "S":
                start = (x, y)

    print(find_loop(start, pipes))



if __name__ == "__main__":
    raise SystemExit(main())

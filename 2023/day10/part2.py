#!/usr/local/bin/python3

from collections import defaultdict

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def adj(x, y, graph):
    c = graph[(x, y)]
    #North
    if c in "L|J" and graph[(x-1, y)] in "|F7":
        yield (x-1, y)
    #South
    if c in "F|7" and graph[(x+1, y)] in "|LJ":
        yield (x+1, y)
    #East
    if c in "J-7" and graph[(x, y-1)] in "-LF":
        yield (x, y-1)
    #West
    if c in "L-F" and graph[(x, y+1)] in "-J7":
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
        while y < M:
            curr = (x, y)
            if curr in loop:
                print(bcolors.OKCYAN+pipes[curr]+bcolors.ENDC, end="")
                if pipes[curr] in "|":
                    inside = not inside
                elif pipes[curr] in "LF":
                    prev = pipes[curr]
                else:
                    if (prev == "F" and pipes[curr] == "J") \
                    or (prev == "L" and pipes[curr] == "7"):
                        inside = not inside
                        prev = None
            elif inside:
                print(bcolors.OKGREEN+pipes[curr]+bcolors.ENDC, end="")
                total += 1
            else:
                print(bcolors.WARNING+pipes[curr]+bcolors.ENDC, end="")
            y += 1
        print("")
    return total

def main():
    with open("input.txt") as f:
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

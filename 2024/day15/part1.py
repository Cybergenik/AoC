#!/usr/local/bin/python3

from collections import defaultdict
#from collections import Counter

def print_board(graph, N, M):
    for y in range(M):
        for x in range(N):
            print(graph[(x,y)], end="")
        print("")
    print("")

def next_move(graph, x, y, dir):
    if dir == "^":
        return (x, y-1), graph[(x, y-1)]
    if dir == "v":
        return (x, y+1), graph[(x, y+1)]
    if dir == ">":
        return (x+1, y), graph[(x+1, y)]
    if dir == "<":
        return (x-1, y), graph[(x-1, y)]

def move(graph, obj, mvs):
    moved = False
    prev = obj
    for dir in mvs:
        loc, o = next_move(graph, *prev, dir)
        if o == ".":
            moved = True
            graph[loc] = graph[prev] 
            graph[prev] = "."
            prev = loc
        elif o == "O":
            if move(graph, loc, [dir]):
                moved = True
                graph[loc] = graph[prev] 
                graph[prev] = "."
                prev = loc
    return moved

def main():
    with open("input.txt") as f:
        content = f.read()
    
    p1, p2 = content.split("\n\n")
    
    graph = defaultdict(lambda: "#")
    mvs = []
    robot = None
    M = len(p1.split("\n"))
    N = len(p1.split("\n")[0])
    for y, l in enumerate(p1.split("\n")):
        for x, c in enumerate(l):
            graph[(x,y)] = c
            if c == "@":
                robot = (x,y)

    for l in p2.split("\n"):
        mvs += [c for c in l.strip()]
    
    move(graph, robot, mvs)
    print_board(graph, N, M)
    print(sum((y*100)+x for (x,y) in graph if graph[(x,y)] == "O"))

if __name__ == "__main__":
    raise SystemExit(main())

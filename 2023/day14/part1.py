#!/usr/local/bin/python3

from collections import defaultdict

def count(map, N, M):
    total = 0
    for x in range(N):
        for y in range(M):
            if map[(x, y)] == "O":
                total += N-x
    return total

def count_north(map, N, M):
    total = 0
    for x in range(N):
        for y in range(M):
            if map[(x, y)] == "O":
                total += 1
                for dx in range(1, N):
                    if map[(dx, y)] == "O":
                        total += 1
                    else:
                        break
        print(total)
    return total

def roll_north(map, N, M):
    for x in range(1, N):
        for y in range(M):
            curr = (x,y)
            if map[curr] == "O":
                while curr[0] > 0:
                    up = (curr[0]-1, curr[1])
                    if map[up] == ".":
                        map[up] = "O"
                        map[curr] = "."
                    else:
                        break
                    curr = up

def print_map(map, N, M):
    for x in range(N):
        for y in range(M):
            print(map[(x,y)], end="")
        print("")
    print("")

def main():
    with open("input.txt") as f:
        content = f.readlines()
    map = defaultdict(lambda: "")
    N = len(content)
    M = len(content[0].strip())
    for x, l in enumerate(content):
        for y, c in enumerate(l.strip()):
            map[(x,y)] = c
    roll_north(map, N, M)
    print_map(map, N, M)
    print(count(map, N, M))
    
if __name__ == "__main__":
    raise SystemExit(main())

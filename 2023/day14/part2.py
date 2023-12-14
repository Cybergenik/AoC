#!/usr/local/bin/python3

from collections import defaultdict
from tqdm import tqdm

def count(map, N, M):
    total = 0
    for x in range(N):
        for y in range(M):
            if map[(x, y)] == "O":
                total += N-x
    return total

def roll_cycle(map, N, M):
    #North
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
    #West
    for y in range(1, M):
        for x in range(N):
            curr = (x,y)
            if map[curr] == "O":
                while curr[1] > 0:
                    left = (curr[0], curr[1]-1)
                    if map[left] == ".":
                        map[left] = "O"
                        map[curr] = "."
                    else:
                        break
                    curr = left
    #South
    for x in range(N-2, -1, -1):
        for y in range(M):
            curr = (x,y)
            if map[curr] == "O":
                while curr[0] < N:
                    down = (curr[0]+1, curr[1])
                    if map[down] == ".":
                        map[down] = "O"
                        map[curr] = "."
                    else:
                        break
                    curr = down
    #East
    for y in range(M-2, -1, -1):
        for x in range(N):
            curr = (x,y)
            if map[curr] == "O":
                while curr[1] < M:
                    right = (curr[0], curr[1]+1)
                    if map[right] == ".":
                        map[right] = "O"
                        map[curr] = "."
                    else:
                        break
                    curr = right

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

    for _ in tqdm(range(N*10)):
        roll_cycle(map, N, M)
    print(count(map, N, M))
    
if __name__ == "__main__":
    raise SystemExit(main())

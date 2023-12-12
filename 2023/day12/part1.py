#!/usr/local/bin/python3

from tqdm import tqdm
from copy import copy

def fits(line, arr):
    curr = 0
    prev = "."
    for c in line:
        if c == "#":
            if curr >= len(arr):
                return 0
            arr[curr] -= 1
            if arr[curr] < 0:
                return 0
        elif c == ".":
            if prev == "#":
                curr += 1
        prev = c
    if sum(arr) != 0:
        return 0
    return 1

def find_perms(line, i, arr):
    if "?" not in line:
        return fits(line, copy(arr))
    total = 0
    while i < len(line) and line[i] != "?":
        i += 1
    line1 = copy(line)
    line1[i] = "#"
    total += find_perms(line1, i+1, arr)
    line2 = copy(line)
    line2[i] = "."
    total += find_perms(line2, i+1, arr)
    return total
        
def main():
    with open("input.txt") as f:
        content = f.readlines()
            
    total = 0
    for l in tqdm(content):
        pattern, arr = l.strip().split()
        pattern = list(pattern)
        arr = list(map(int, arr.split(",")))
        total += find_perms(pattern, 0, arr)
        
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

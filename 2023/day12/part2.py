#!/usr/local/bin/python3

from tqdm import tqdm
from copy import copy

def find_perms(line, i, prev, arr):
    while i < len(line) and line[i] != "?":
        if line[i] == "#":
            if len(arr) == 0:
                return 0
            arr[0] -= 1
            if arr[0] < 0:
                return 0
        elif line[i] == "." and prev == "#":
            if arr.pop(0) > 0:
                return 0
            if len(arr) == 0:
                return 1
        prev = line[i]
        i += 1
    if i < len(line) and len(arr) > 0:
        total = 0
        if prev == "#" and arr[0] > 0:
            arr1 = copy(arr)
            arr1[0] -= 1
            total += find_perms(line, i+1, "#", arr1)
        elif prev == "#" and arr[0] == 0:
            total += find_perms(line, i+1, ".", arr[1:])
        else:
            arr1 = copy(arr)
            arr1[0] -= 1
            total += find_perms(line, i+1, "#", arr1)
            total += find_perms(line, i+1, ".", arr)
        return total
    return 1

        
def main():
    with open("test.txt") as f:
        content = f.readlines()
            
    total = 0
    for l in tqdm(content):
        pattern, arr = l.strip().split()
        pattern = list(pattern)
        arr = list(map(int, arr.split(",")))
        OGP = copy(pattern)
        OGR = copy(arr)
        for i in range(4):
            pattern.append("?")
            pattern.extend(OGP)
            arr.extend(OGR)
        juice = find_perms(pattern, 0, ".", arr)
        print(juice)
        total += juice
    
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

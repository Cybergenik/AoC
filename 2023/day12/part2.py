#!/usr/local/bin/python3

from tqdm import tqdm
from copy import copy

def key(i, arr, j):
    return str(i)+"".join(map(str, arr))+str(j)

def find_perms(line, i, arr, j, prev, cache):
    k = key(i, arr, j)
    if k not in cache:
        while i < len(line) and line[i] != "?":
            if line[i] == "#":
                if j < len(arr) and arr[j] > 0:
                    arr[j] -= 1
                else:
                    return 0
            elif line[i] == '.':
                if prev == "#":
                    if arr[j] == 0:
                        j += 1
                    else:
                        return 0
            prev = line[i]
            i += 1
        if i == len(line):
            return sum(arr) == 0
        if j == len(arr):
            if "#" in line[i:]:
                return 0
            else:
                return 1
        total = 0
        if prev == "#":
            if arr[j] > 0:
                arr1 = copy(arr)
                arr1[j] -= 1
                total += find_perms(line, i+1, arr1, j, "#", cache)
            else:
                total += find_perms(line, i+1, arr, j+1, ".", cache)
        else:
            arr1 = copy(arr)
            arr1[j] -= 1
            total += find_perms(line, i+1, arr1, j, "#", cache)
            total += find_perms(line, i+1, arr, j, ".", cache)
        cache[k] = total
    return cache[k]
        
def main():
    with open("input.txt") as f:
        content = f.readlines()
            
    total = 0
    for l in tqdm(content):
        pattern, arr = l.strip().split()
        arr = list(map(int, arr.split(",")))
        OGP = pattern
        OGR = copy(arr)
        for i in range(4):
            pattern += "?"
            pattern += OGP
            arr.extend(OGR)
        total += find_perms(pattern, 0, arr, 0, None, {})
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

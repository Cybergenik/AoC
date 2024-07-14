#!/usr/local/bin/python3

from tqdm import tqdm
from copy import copy

def find_perms(line, i, arr, j, prev):
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
            total += find_perms(line, i+1, arr1, j, "#")
        else:
            total += find_perms(line, i+1, arr, j+1, ".")
    else:
        arr1 = copy(arr)
        arr1[j] -= 1
        total += find_perms(line, i+1, arr1, j, "#")
        total += find_perms(line, i+1, arr, j, ".")
    return total
        
def main():
    with open("input.txt") as f:
        content = f.readlines()
    total = 0
    for l in tqdm(content):
        pattern, arr = l.strip().split()
        arr = list(map(int, arr.split(",")))
        pos = find_perms(pattern, 0, arr, 0, None)
        total += pos
        
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

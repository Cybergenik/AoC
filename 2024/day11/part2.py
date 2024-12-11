#!/usr/local/bin/python3

from collections import defaultdict
from functools import cache
#from collections import Counter

@cache
def count_stones(stone, blink):
    if blink == 75:
        return 1
    if stone == 0:
        return count_stones(1, blink+1)
    elif len(str(stone)) % 2 == 0:
        n = str(stone)
        mid = len(n)//2
        l, r = n[:mid], n[mid:]
        return count_stones(int(l), blink+1) + count_stones(int(r), blink+1)
    else:
        return count_stones(stone*2024, blink+1)

def blinks(stones):
    total = 0
    for s in stones:
        total += count_stones(s, 0)
    return total

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    stones = list(map(int, content[0].strip().split()))
    print(blinks(stones))
        
if __name__ == "__main__":
    raise SystemExit(main())

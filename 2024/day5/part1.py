#!/usr/local/bin/python3

from collections import defaultdict
#from functools import cache
#from collections import Counter

def check_order(graph, nums):
    for i, v in enumerate(nums):
        for u in graph[v]:
            if u in nums[i+1:]:
                return False
    return True

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    total = 0
    out_graph = defaultdict(lambda: [])
    in_graph = defaultdict(lambda: [])
    part1 = True
    for l in content:
        if l == "\n":
            part1 = False
        elif part1:
            l, r = l.strip().split("|")
            in_graph[int(r)].append(int(l))
            out_graph[int(l)].append(int(r))
        else:
            nums = list(map(int, l.strip().split(",")))
            if check_order(in_graph, nums):
                total += nums[len(nums)//2]
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

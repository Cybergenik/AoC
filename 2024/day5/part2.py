#!/usr/local/bin/python3

from collections import defaultdict
#from functools import cache
#from collections import Counter

def topo(graph, nums):
    def dfs(u):
        if u not in seen:
            seen.add(u)
            for v in graph[u]:
                if v in nums:
                    dfs(v)
            order.append(u)
    seen = set()
    order = []
    for u in nums:
        if u not in seen:
            dfs(u)
    return order

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
    graph = defaultdict(lambda: [])
    part1 = True
    for l in content:
        if l == "\n":
            part1 = False
        elif part1:
            l, r = l.strip().split("|")
            graph[int(r)].append(int(l))
        else:
            nums = list(map(int, l.strip().split(",")))
            if not check_order(graph, nums):
                ordered_nums = topo(graph, nums)
                total += ordered_nums[len(ordered_nums)//2]
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

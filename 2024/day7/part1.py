#!/usr/local/bin/python3

from collections import defaultdict
import itertools
#from functools import cache
#from collections import Counter

def all_combos(nums):
    ops = "+*"
    for c in itertools.product(ops, repeat=len(nums)-1):
        seq = ["("]*len(c)
        curr_c = 0
        for n in nums:
            seq.append(n)
            if curr_c > 0:
               seq.append(")")
            if curr_c < len(c):
                seq.append(c[curr_c])
                curr_c += 1
        yield seq

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    total = 0
    ops = defaultdict(lambda: [])
    for l in content:
        t, nums = l.strip().split(":")
        nums = nums.strip().split()
        ops[int(t)] = list(map("".join, all_combos(nums)))
    for k, eqs in ops.items():
        for eq in eqs:
            if k == eval(eq):
                total += k
                break
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

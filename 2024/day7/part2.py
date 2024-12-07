#!/usr/local/bin/python3

from tqdm import tqdm
from collections import defaultdict
import itertools

class Num:
    def __init__(self, x):
        self.x = x
    def __mul__(self, x):
        return Num(self.x*x.x)
    def __add__(self, x):
        return Num(self.x+x.x)
    def __or__(self, x):
        return Num(int(f"{self.x}{x.x}"))
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

def all_combos(nums):
    ops = "+*|"
    for c in itertools.product(ops, repeat=len(nums)-1):
        seq = ["("]*len(c)
        curr_c = 0
        for n in nums:
            seq.append(f"Num({n})")
            if curr_c > 0:
               seq.append(")")
            if curr_c < len(c):
                seq.append(c[curr_c])
                curr_c += 1
        yield seq

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    total = Num(0)
    ops = defaultdict(lambda: [])
    for l in tqdm(content):
        t, nums = l.strip().split(":")
        nums = nums.strip().split()
        ops[Num(int(t))] = list(map("".join, all_combos(nums)))
    for k, eqs in tqdm(ops.items()):
        for eq in eqs:
            if k == eval(eq):
                total += k
                break
    print(total.x)

if __name__ == "__main__":
    raise SystemExit(main())

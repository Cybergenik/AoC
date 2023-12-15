#!/usr/local/bin/python3

from collections import deque, defaultdict
from pprint import pprint

class HashMap():
    def __init__(self):
        self.map = defaultdict(lambda: deque())

    def add(self, op):
        h = self.hash(op[0])
        loc = None
        old = None
        for i, old_op in enumerate(self.map[h]):
            if old_op[0] == op[0]:
                loc = i
                old = old_op
                break
        if old:
            self.map[h].remove(old)
            self.map[h].insert(loc, op)
        else:
            self.map[h].append(op)

    def remove(self, name):
        h = self.hash(name)
        rm = None
        for op in self.map[h]:
            if op[0] == name:
                rm = op
                break
        if rm:
            self.map[h].remove(rm)

    def get_focusing_power(self):
        total = 0
        for ops in self.map.values():
            for i, op in enumerate(ops):
                power = self.hash(op[0])+1
                power *= (i+1)
                power *= op[1]
                total += power
        return total

    def hash(self, s):
        h = 0
        for c in s:
            h += ord(c)
            h *= 17
            h %= 256
        return h

def main():
    with open("input.txt") as f:
        content = f.readlines()
    steps = content[0].strip().split(",")
    hm = HashMap()
    for s in steps:
        if "=" in s:
            name, fl = s.split("=")
            hm.add((name, int(fl)))
        elif "-" in s:
            name = s.split("-")[0]
            hm.remove(name)

    pprint(hm.map)
    print(hm.get_focusing_power())

if __name__ == "__main__":
    raise SystemExit(main())

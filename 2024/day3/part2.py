#!/usr/local/bin/python3

#from functools import lru_cache
#from collections import Counter
import re

def mul(l):
    l, r = l.split(",")
    l = l.split("(")[-1]
    r = r.split(")")[0]
    return int(l) * int(r)

def main():
    with open("input.txt") as f:
        content = f.read()
       
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    total = 0
    insts = content.strip()
    all_dos = [match.start() for match in re.finditer(do_pattern, insts)]
    all_donts = [match.start() for match in re.finditer(dont_pattern, insts)]
    prev_loc = -1
    prev_allowed = True
    for match in re.finditer(mul_pattern, insts):
        while len(all_dos) > 0 and match.start() > all_dos[0]:
            if prev_loc < all_dos[0]:
                prev = all_dos.pop(0)
                prev_allowed = True
        while len(all_donts) > 0 and match.start() > all_donts[0]:
            if prev_loc < all_donts[0]:
                prev = all_donts.pop(0)
                prev_allowed = False
        if prev_allowed:
            total += mul(match[0])
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

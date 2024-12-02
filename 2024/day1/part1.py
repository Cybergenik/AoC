#!/usr/local/bin/python3

#from functools import lru_cache
#from collections import Counter

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    ls = []
    rs = []
    for l in content:
        ln, rn = l.strip().split("   ")
        ls.append(int(ln))
        rs.append(int(rn))

    total = 0
    for v1, v2 in zip(sorted(ls), sorted(rs)):
        total += abs(v1 - v2)
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

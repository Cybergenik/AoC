#!/usr/local/bin/python3

from collections import Counter

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
    rsc = Counter(rs)
    for v1 in sorted(ls):
        total += v1 * rsc[v1]
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

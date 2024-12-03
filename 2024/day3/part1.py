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
    total = 0
    for match in re.finditer(mul_pattern, content.strip()):
        total += mul(match[0])
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

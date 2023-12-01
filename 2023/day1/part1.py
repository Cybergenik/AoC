#!/usr/local/bin/python3

#from functools import lru_cache
#from collections import Counter

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    total = 0
    for l in content:
        l = l.strip()
        num = ""
        for c in l:
            if str(c).isnumeric():
                num += c
                break
        for c in l[::-1]:
            if c.isnumeric():
                num += c
                break
        total += int(num)
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

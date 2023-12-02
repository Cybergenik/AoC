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
        last = ""
        for c in l:
            if c.isnumeric():
                if num == "":
                    num += c
                last = c
        total += int(num+last)
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

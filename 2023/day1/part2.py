#!/usr/local/bin/python3

#from functools import lru_cache
#from collections import Counter

def number(line: str):
    if line.startswith("one"):   return "1"
    if line.startswith("two"):   return "2"
    if line.startswith("three"): return "3"
    if line.startswith("four"):  return "4"
    if line.startswith("five"):  return "5"
    if line.startswith("six"):   return "6"
    if line.startswith("seven"): return "7"
    if line.startswith("eight"): return "8"
    if line.startswith("nine"):  return "9"
    return None

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    total = 0
    for l in content:
        l = l.strip()
        num = ""
        last = ""
        for i, c in enumerate(l):
            if c.isnumeric():
                if num == "":
                    num += c
                last = c
            elif number(l[i:]) is not None:
                if num == "":
                    num += number(l[i:])
                last = number(l[i:])
        total += int(num+str(last))
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/local/bin/python3

#from functools import lru_cache
#from collections import Counter

def number(line):
    if "one" in line:
        return "1"
    if "two" in line:
        return "2"
    if "three" in line:
        return "3"
    if "four" in line:
        return "4"
    if "five" in line:
        return "5"
    if "six" in line:
        return "6"
    if "seven" in line:
        return "7"
    if "eight" in line:
        return "8"
    if "nine" in line:
        return "9"
    return None

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    total = 0
    for l in content:
        l = l.strip()
        num = ""
        for i, c in enumerate(l):
            if str(c).isnumeric():
                num += c
                break
            real = number(l[:i+1])
            if real is not None:
                num += real
                break
        for i in range(len(l)-1, -1, -1):
            if l[i].isnumeric():
                num += l[i]
                break
            real = number(l[i:])
            if real is not None:
                num += real
                break
        print(num)
        total += int(num)
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

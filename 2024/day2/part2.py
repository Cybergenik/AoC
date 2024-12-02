#!/usr/local/bin/python3

#from functools import lru_cache
#from collections import Counter

def check_seq(li):
    incr = None
    for n1, n2 in zip(li[:-1], li[1:]):
        if n1 < n2:
            if incr == None:
                incr = True
            elif incr == False:
                return False
        if n1 > n2:
            if incr == None:
                incr = False
            elif incr == True:
                return False
        if n1 == n2:
            return False
        diff = abs(n1 - n2) 
        if diff < 1 or diff > 3:
            return False
    return True

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    total = 0
    for l in content:
        l = l.strip()
        li = list(map(int, l.split()))
        if check_seq(li):
            total += 1
        else:
            for i in range(len(li)):
                if check_seq(li[:i] + li[i+1:]):
                    total += 1
                    break
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

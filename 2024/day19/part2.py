#!/usr/local/bin/python3

from functools import cache
 
def possible_designs(patterns, designs):
    @cache
    def possible(des):
        if len(des) == 0:
            return 1
        total = 0
        for i in range(1, len(des)+1):
            subd = des[:i]
            if subd in patterns:
                total += possible(des[i:])
        return total
    
    total = 0
    for d in designs:
        total += possible(d)
    return total

def main():
    with open("input.txt") as f:
        content = f.read()
    
    pat, designs = content.split("\n\n")
    pat = pat.strip().split(", ")
    designs = designs.strip().split("\n")
    print(possible_designs(set(pat), designs))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

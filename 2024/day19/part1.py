#!/usr/local/bin/python3

from functools import cache
 
def possible_designs(patterns, designs):
    @cache
    def possible(des):
        if len(des) == 0:
            return True
        for i in range(1, len(des)+1):
            subd = des[:i]
            if subd in patterns and possible(des[i:]):
                return True
        return False
    
    total = 0
    for d in designs:
        if possible(d):
            total += 1
    return total

def main():
    with open("input.txt") as f:
        content = f.read()
    
    pat, designs = content.split("\n\n")
    pat = pat.strip().split(", ")
    designs = [d for d in designs.strip().split("\n")]
    print(possible_designs(set(pat), designs))

if __name__ == "__main__":
    raise SystemExit(main())

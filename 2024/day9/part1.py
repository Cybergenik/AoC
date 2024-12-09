#!/usr/local/bin/python3

from collections import defaultdict
#from functools import cache
#from collections import Counter

def compact_fs(fs):
    enlarged = []
    ip = 0
    for i, n in enumerate(fs):
        if i % 2 == 0:
            enlarged += [ip]*n
            ip += 1
        else:
            enlarged += ['.']*n
    i, j = 0, len(enlarged)-1
    new_fs = []
    seen = set()
    while i <= j:
        if enlarged[i] == '.':
            while enlarged[j] == '.':
                j -= 1
            if i < j:
                new_fs.append(enlarged[j])
                seen.add(j)
                j -= 1
        else:
            new_fs.append(enlarged[i])
        i+=1
    return new_fs

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    fs = []
    for c in content[0].strip():
        fs.append(int(c))
    nfs = compact_fs(fs)
    total = 0
    for i, n in enumerate(nfs):
        total += i * n
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

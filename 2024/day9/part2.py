#!/usr/local/bin/python3

from collections import defaultdict
#from functools import cache
#from collections import Counter

def compact_fs(fs):
    nfs = []
    used_space = []
    free_space = []
    ip = 0
    for i, n in enumerate(fs):
        if n == 0:
            continue
        if i % 2 == 0:
            used_space.append((len(nfs), n))
            nfs += [ip]*n
            ip += 1
        else:
            free_space.append((len(nfs), n))
            nfs += ['.']*n
    i = len(used_space)-1
    while i > 0:
        u = used_space[i]
        for j in range(len(free_space)):
            e = free_space[j]
            if e[0] > u[0]:
                break
            if e[1] >= u[1]:
                diff = e[1]-u[1]
                nfs[e[0]:e[0]+e[1]] = nfs[u[0]:u[0]+u[1]] + ['.']*diff
                nfs[u[0]:u[0]+u[1]] = ['.']*u[1]
                free_space[j] = (e[0]+e[1]-diff, diff)
                break
        i -= 1
    return nfs

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    fs = []
    for c in content[0].strip():
        fs.append(int(c))
    nfs = compact_fs(fs)
    total = 0
    for i, n in enumerate(nfs):
        if n == '.':
            continue
        total += i * n
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

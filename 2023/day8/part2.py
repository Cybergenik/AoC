#!/usr/local/bin/python3

def main():
    with open("input.txt") as f:
        content = f.readlines()
    map = {}
    currs = []
    inst = content[0].strip()
    for l in content[2:]:
        l = l.strip()
        n, vv = l.split(" = ")
        left, right = vv.split(", ")
        left, right = left[1:], right[:-1]
        map[n] = (left, right)
        if n[-1] == "A":
            currs.append(n)
    
    steps = 0
    while True:
        for i in inst:
            found = 0
            for j, c in enumerate(currs):
                if i == "R":
                    currs[j] = map[c][1]
                if i == "L":
                    currs[j] = map[c][0]
                if c[-1] == "Z":
                    found += 1
            if found == len(currs):
                print(steps)
                return
            steps += 1

if __name__ == "__main__":
    raise SystemExit(main())

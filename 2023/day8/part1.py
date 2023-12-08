#!/usr/local/bin/python3

def main():
    with open("input.txt") as f:
        content = f.readlines()
    map = {}

    inst = content[0].strip()
    for l in content[2:]:
        l = l.strip()
        n, vv = l.split(" = ")
        left, right = vv.split(", ")
        left, right = left[1:], right[:-1]
        map[n] = (left, right)
    
    curr = "AAA"
    total = 0
    while curr != "ZZZ":
        for i in inst:
            if i == "R":
                curr = map[curr][1]
            if i == "L":
                curr = map[curr][0]
            total += 1
    print(total)
        

if __name__ == "__main__":
    raise SystemExit(main())

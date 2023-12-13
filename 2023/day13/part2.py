#!/usr/local/bin/python3

def off_by_one(left, right):
    one = False
    for l, r in zip(left, right):
        if l != r:
            if not one:
                one = True
            else:
                return False
    return True
        
def check_ref(map):
    for i in range(len(map)-1):
        smudge = True
        l, r = i, i+1
        while l >= 0 and r < len(map):
            if map[l] != map[r]:
                if smudge and off_by_one(map[l], map[r]):
                    smudge = False
                else:
                    break
            l -= 1
            r += 1
        if (r == len(map) or l < 0) and not smudge:
            return i+1
    return 0

def main():
    with open("input.txt") as f:
        content = f.readlines()
    maps = []
    curr_map = []
    for x, l in enumerate(content):
        if l.strip() == "":
            maps.append(curr_map)
            curr_map = []
        else:
            curr_map.append(l.strip())
    maps.append(curr_map)

    total = 0
    for m in maps:
        rmap = ["".join(l) for l in zip(*m[::-1])]
        hori = check_ref(m)
        if hori > 0:
            total += 100*hori
        else:
            total += check_ref(rmap)
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

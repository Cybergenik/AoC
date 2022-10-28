from collections import defaultdict
def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    lines = [x.strip().split(" | ") for x in content]
    # 1 -> len == 2
    # 4 -> len == 4
    # 7 -> len == 3
    # 8 -> len == 7
    uniques = set([2,4,3,7])
    
    # 0 -> len == 6
    # 2 -> len == 5
    # 3 -> len == 5
    # 5 -> len == 5
    # 6 -> len == 6
    # 9 -> len == 6
    total = 0
    for sequences in lines:
        keys = defaultdict(set)
        unknown = sequences[0].split()
        while unknown:
            curr_s = unknown.pop()
            curr = set([x for x in curr_s])
            if len(curr) == 2:
                keys[1] = curr
            elif len(curr) == 4:
                keys[4] = curr 
            elif len(curr) == 3:
                keys[7] = curr
            elif len(curr) == 7:
                keys[8] = curr
            elif len(curr) == 5 and keys[1] and keys[4]:
                if len(keys[1] - curr) == 0:
                    keys[3] = curr
                elif len(keys[4] - curr) == 1:
                    keys[5] = curr
                else: 
                    keys[2] = curr
            elif len(curr) == 6 and keys[7] and keys[4]:
                if len(keys[7] - curr) == 1:
                    keys[6] = curr
                elif len(keys[4] - curr) == 0:
                    keys[9] = curr
                else:
                    keys[0] = curr
            else:
                unknown.insert(0, curr_s)
        num = ""
        vals = {"".join(sorted(list(v))):k for k,v in keys.items()}
        for out in sequences[1].split():
            curr = "".join(sorted(out))
            num += str(vals[curr])
        total += int(num)
    print(total)
if __name__ == "__main__":
    raise SystemExit(main())

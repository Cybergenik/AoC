import ast 

def compare(l:list, r:list):
    for i in range(min(len(l), len(r))):
        # base:
        if isinstance(l[i], int) and isinstance(r[i], int):
            if l[i] < r[i]:
                return 1
            elif l[i] > r[i]:
                return -1
        # rec:
        else:
            if isinstance(l[i], int):
                l[i] = [l[i]]
            elif isinstance(r[i], int):
                r[i] = [r[i]]
            rec_cmp = compare(l[i], r[i])
            if rec_cmp != 0:
                return rec_cmp
    if len(l) < len(r): 
        return 1
    elif len(l) > len(r):
        return -1
    else:
        return 0

def main() -> int:
    with open("input.txt") as f:
        content = f.read()

    total = 0
    pairs = content.split("\n\n")
    for i, pair in enumerate(pairs):
        l, r = pair.strip('\n').split("\n")
        pl = ast.literal_eval(l)
        pr = ast.literal_eval(r)
        if compare(pl, pr) >= 0:
            total += i+1

    print(total)
if __name__ == "__main__":
    raise SystemExit(main())


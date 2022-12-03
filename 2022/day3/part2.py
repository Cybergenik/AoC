from collections import Counter

def get_val(x: str):
    if x.islower():
        return (ord(x)-96)
    else:
        return (ord(x)-65)+27

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    
    total = 0
    currs = None
    i = 0
    for l in content:
        i += 1
        l = l.strip()
        # 10 // 2 = 5
        f = set(list(l))
        if not currs:
            currs = f
        else:
            currs = currs & f
        if i % 3 == 0:
            v = list(currs)[0]
            currs = None
            total += get_val(v)
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

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
    for l in content:
        l = l.strip()
        # 10 // 2 = 5
        f = set(l[:len(l)//2])
        s = set(l[len(l)//2:])
        shared = f & s
        if shared:
            v = list(shared)[0]
            total += get_val(v)
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

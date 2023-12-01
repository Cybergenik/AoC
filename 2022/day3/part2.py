
def get_val(x: str):
    if x.islower():
        return (ord(x)-96)
    else:
        return (ord(x)-65)+27

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    total = 0
    currs = None
    for i, l in enumerate(content):
        l = l.strip()
        f = set(list(l))
        if not currs:
            currs = f
        else:
            currs = currs & f
        i += 1
        if i % 3 == 0:
            v = list(currs)[0]
            currs = None
            total += get_val(v)
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

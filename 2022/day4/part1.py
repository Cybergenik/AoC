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
        l, r = l.split(',')
        fl, sl = l.split("-")
        fl, sl = int(fl), int(sl)
        f_set = set(list(range(fl, sl+1)))
        fr, sr = r.split("-")
        fr, sr = int(fr), int(sr)
        s_set = set(list(range(fr, sr+1)))
        if (f_set & s_set) == f_set or (f_set & s_set) == s_set:
            total += 1
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

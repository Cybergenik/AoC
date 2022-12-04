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
        if len(f_set & s_set) > 0:
            total += 1
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

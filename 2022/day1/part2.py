
def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    all = []
    curr = 0
    for l in content:
        l = l.strip()
        if l == "":
            all.append(curr)
            curr = 0
            continue
        curr += int(l)
    all.append(curr)
    print(sum(sorted(all, reverse=True)[:3]))

if __name__ == "__main__":
    raise SystemExit(main())

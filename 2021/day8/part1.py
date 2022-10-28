def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    lines = [x.strip().split(" | ") for x in content]
    # 1 -> len == 2
    # 4 -> len == 4
    # 7 -> len == 3
    # 8 -> len == 7
    uniques = set([2,4,3,7])
    total = 0
    for l in lines:
        for out in l[1].split():
            if len(out) in uniques:
                total += 1
    print(total)
if __name__ == "__main__":
    raise SystemExit(main())

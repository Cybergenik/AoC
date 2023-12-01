
def main():
    with open("input.txt") as f:
        content = f.readlines()
    max_ = 0
    curr = 0
    content.split("\n\n")
    for l in content:
        l = l.strip()
        if l == "":
            if curr > max_:
                max_ = curr
            curr = 0
            continue
        curr += int(l)
    if curr > max_:
        max_ = curr
    print(max_)

if __name__ == "__main__":
    raise SystemExit(main())

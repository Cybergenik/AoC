def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()

    lines = [(str(line.split()[0]), int(line.split()[1])) for line in content]
    depth = 0
    horizontal = 0
    for l in lines:
        if l[0] == "forward":
            horizontal += l[1]
        elif l[0] == "up":
            depth -= l[1]
        elif l[0] == "down":
            depth += l[1]
    print(depth*horizontal)

if __name__ == "__main__":
    raise SystemExit(main())

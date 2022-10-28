
def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    freq = 0
    for l in content:
        freq += int(l.strip())
    print(freq)

if __name__ == "__main__":
    raise SystemExit(main())

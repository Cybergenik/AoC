
def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()

    seen = {0}
    freq = 0
    while True:
        for l in content:
            freq += int(l.strip())
            if freq in seen:
                print(freq)
                return
            seen.add(freq)

if __name__ == "__main__":
    raise SystemExit(main())

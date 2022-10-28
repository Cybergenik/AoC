from collections import Counter

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()

    three = 0
    two = 0
    for l in content:
        c = Counter(l.strip())
        seen3 = False
        seen2 = False
        for letter, count in c.items():
            if not seen2 and count == 2:
                seen2 = True
                two += 1
            if not seen3 and count == 3:
                seen3 = True
                three += 1
    print(three*two)

if __name__ == "__main__":
    raise SystemExit(main())

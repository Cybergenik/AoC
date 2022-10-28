from statistics import mean

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    crabs = [int(x) for x in content[0].split(",")]
    
    mid = int(mean(crabs))
    total = 0
    for c in crabs:
        total += sum(range(1, abs(c - mid)+1))
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

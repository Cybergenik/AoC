from statistics import median

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    crabs = [int(x) for x in content[0].split(",")]
    
    total = 0
    for i in crabs:
        curr = 0
        for j in crabs:
            curr += abs(i - j)
        if curr < total or total == 0:
            total = curr
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()

    map_territory: list[list] = [[0 for x in range(1000)] for l in range(1000)]
    for i in content:
        line = i.strip().split(" -> ")
        left = line[0].split(",")
        right = line[1].split(",")
        x = (int(left[0]), int(left[1]))
        y = (int(right[0]), int(right[1]))
        if x[0] == y[0]:
            curr = min(x[1], y[1])
            end = max(x[1], y[1])
            while curr <= end:
                map_territory[x[0]][curr] += 1
                curr += 1
        elif x[1] == y[1]:
            curr = min(x[0], y[0])
            end = max(x[0], y[0])
            while curr <= end:
                map_territory[curr][x[1]] += 1
                curr += 1

    total = 0
    for i in map_territory:
        total += len([x for x in i if x >= 2])
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())


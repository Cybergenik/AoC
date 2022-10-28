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

        curr_x = x[0]
        curr_y = x[1]
        map_territory[y[0]][y[1]] += 1
        while curr_x != y[0] or curr_y != y[1]:
            map_territory[curr_x][curr_y] += 1

            if curr_x < y[0]:
                curr_x += 1
            elif curr_x > y[0]:
                curr_x -= 1

            if curr_y < y[1]:
                curr_y += 1
            elif curr_y > y[1]:
                curr_y -= 1

    total = 0
    for i in map_territory:
        total += len([x for x in i if x >= 2])
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())
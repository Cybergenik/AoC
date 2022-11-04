from collections import defaultdict

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    coords = []
    for l in content:
        l = l.strip()
        x, y = l.split(",")
        coords.append((int(x),int(y.strip())))

    #Define borders
    GRID_N = 500
    total = 0
    for i in range(GRID_N):
        for j in range(GRID_N):
            dist_total = 0
            for k, (x,y) in enumerate(coords):
                man_dist = abs(i-x) + abs(j-y)
                dist_total += man_dist
            if dist_total < 10000:
                total += 1

    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

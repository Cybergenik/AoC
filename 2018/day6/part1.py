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
    areas = defaultdict(lambda: 0)
    infinites = set()
    for i in range(GRID_N):
        for j in range(GRID_N):
            dists = []
            for k, (x,y) in enumerate(coords):
                man_dist = abs(i-x) + abs(j-y)
                dists.append((k, man_dist))
            dists.sort(key=lambda x: x[1])
            if dists[0][1] == dists[1][1]:
                continue
            if i < GRID_N-1 and i > 0 and j < GRID_N-1 and j > 0:
                areas[dists[0][0]] += 1
            else:
                infinites.add(dists[0][0])

    largest = None
    for k, (x,y) in enumerate(coords):
        if k not in infinites:
            if not largest or areas[k] > largest:
                largest = areas[k]

    print(largest)

if __name__ == "__main__":
    raise SystemExit(main())

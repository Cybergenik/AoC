
def man_dist(v, u):
    return abs(v[0]-u[0]) + abs(v[1]-u[1])

def row_mark(sensor, beacons, dist, row):
    empty = set()
    for i in range(sensor[0], sensor[0]-dist, -1):
        curr = (i, row)
        if man_dist(sensor, curr) > dist:
            break
        if curr not in beacons:
            empty.add(curr)
    for i in range(sensor[0], sensor[0]+dist):
        curr = (i, row)
        if man_dist(sensor, curr) > dist:
            break
        if curr not in beacons:
            empty.add(curr)
    return empty

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    empty = set()
    dists = {}
    sensors = set()
    beacons = set()
    for l in content:
        l = l.strip().split()
        sx = int(l[2].split("=")[1][:-1])
        sy = int(l[3].split("=")[1][:-1])
        bx = int(l[8].split("=")[1][:-1])
        by = int(l[9].split("=")[1])
        s = (sx,sy)
        b = (bx, by)
        dists[s] = man_dist(s, b)
        sensors.add(s)
        beacons.add(b)
    for s in sensors:
        empty |= row_mark(s, beacons, dists[s], 2000000)
    print(len(empty))

if __name__ == "__main__":
    raise SystemExit(main())


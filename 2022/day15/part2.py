from tqdm import tqdm

def man_dist(v, u):
    return abs(v[0]-u[0]) + abs(v[1]-u[1])

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    dists = {}
    sensors = set()
    beacons = set()
    min_x = max_x = 0
    min_y = max_y = 0
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
        min_x = min(sensors, key= lambda x: x[0])
        max_x = max(sensors, key= lambda x: x[0])
        min_y = min(sensors, key= lambda x: x[1])
        max_y = max(sensors, key= lambda x: x[1])

    N = 4_000_000
    for x in tqdm(range(min_x[0]+dists[min_x], max_x[0]-dists[max_x])):
        for y in range(min_y[1]+dists[min_y], max_y[1]-dists[max_y]):
            curr = (x,y)
            if curr in sensors and curr in beacons:
                continue
            found = False
            for s in sensors:
                if man_dist(s, curr) <= dists[s]:
                    found = True
                    break
            if not found:
                print((x*N)+y)

if __name__ == "__main__":
    raise SystemExit(main())


#!/usr/local/bin/python3

maps = []

def get_overlap(r1, r2):
    s1, e1 = r1
    s2, e2 = r2
    # Check for no overlap
    if e1 < s2 or e2 < s1:
        return None  # No overlap

    return (max(s1, s2), min(e1, e2))

class Mapping:
    def __init__(self):
        self.ranges = []
        self.maps = {}
    def add_map_range(self, src, dest, rng):
        self.ranges.append((src, src+rng))
        self.maps[src] = dest
    def get_range(self, rng):
        for r2 in self.ranges:
            overlap = get_overlap(rng, r2)
            if overlap:
                start = self.maps[r2[0]] + (overlap[0] - r2[0])
                end = start + (overlap[1] - overlap[0])
                return (start, end)
        return rng
    def get_ranges(self, src_ranges):
        return [self.get_range(r) for r in src_ranges]
    def get_min(self):
        return min(self.maps.keys(), key=lambda x: self.maps[x])

def get_min(x):
    m1 = maps[0].get_ranges(x)
    m2 = maps[1].get_ranges(m1)
    m3 = maps[2].get_ranges(m2)
    m4 = maps[3].get_ranges(m3)
    m5 = maps[4].get_ranges(m4)
    m6 = maps[5].get_ranges(m5)
    m7 = maps[6].get_ranges(m6)
    print(m7)
    return min(m7)

def main():
    with open("test.txt") as f:
        content = f.readlines()

    seeds = []
    i = 0
    while i < len(content):
        if content[i].startswith("seeds:"):
            l = content[i].strip()
            seedr = l.split(": ")[-1].split()
            for j in range(0, len(seedr), 2):
                seeds.append((int(seedr[j]), int(seedr[j])+int(seedr[j+1])))
        elif content[i].startswith("seed-to-soil map:") \
        or content[i].startswith("soil-to-fertilizer map:") \
        or content[i].startswith("fertilizer-to-water map:") \
        or content[i].startswith("water-to-light map:") \
        or content[i].startswith("light-to-temperature map:") \
        or content[i].startswith("temperature-to-humidity map:") \
        or content[i].startswith("humidity-to-location map:"):
            i += 1
            map = Mapping()
            while i < len(content) and content[i] != "\n":
                dest, src, rng = content[i].strip().split()
                map.add_map_range(int(src), int(dest), int(rng))
                i += 1
            maps.append(map)
        i += 1

    print(get_min(seeds))

if __name__ == "__main__":
    raise SystemExit(main())

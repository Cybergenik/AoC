#!/usr/local/bin/python3

def get_overlap(r1, r2):
    s1, e1 = r1
    s2, e2 = r2
    # Check for no overlap
    if e1 < s2 or e2 < s1:
        return None
    return (max(s1, s2), min(e1, e2))

class Mapping:
    def __init__(self):
        self.ranges = []
    def add_map_range(self, src, dest, rng):
        self.ranges.append((src, dest, rng))
        self.ranges = sorted(self.ranges)
    def get_ranges(self, src_rng):
        rngs = []
        prev = src_rng[0]
        for src, dest, rng in self.ranges:
            overlap = get_overlap(src_rng, (src, src+rng))
            if overlap:
                start = dest + (overlap[0] - src)
                nrng = abs(overlap[1] - overlap[0])
                # add non-mapped range
                if overlap[0] > prev:
                    rngs.append((prev, overlap[0]))
                prev = overlap[1]
                rngs.append((start, start+nrng))
        if prev < src_rng[1]:
            rngs.append((prev, src_rng[1]))
        return rngs
    def get_mapping(self, src_ranges):
        return [ss for s in src_ranges for ss in self.get_ranges(s)]

def get_min(x, maps):
    print("Getting Seed -> Soil...")
    m1 = maps[0].get_mapping(x)
    print("Getting Soil -> Fertilizer...")
    m2 = maps[1].get_mapping(m1)
    print("Getting Fertilizer -> Water...")
    m3 = maps[2].get_mapping(m2)
    print("Getting Water -> Light...")
    m4 = maps[3].get_mapping(m3)
    print("Getting Light -> Temperature...")
    m5 = maps[4].get_mapping(m4)
    print("Getting Temperature -> Humidity...")
    m6 = maps[5].get_mapping(m5)
    print("Getting Humidity -> Location...")
    m7 = maps[6].get_mapping(m6)
    return min(m7)

def main():
    with open("input.txt") as f:
        content = f.readlines()

    maps = []
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

    print(f'Min location of initial seed range: {get_min(seeds, maps)[0]}')

if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/local/bin/python3

maps = []

class Mapping:
    def __init__(self):
        self.ranges = []
        self.maps = {}
    def add_map_range(self, src, dest, rng):
        self.ranges.append((src, src+rng))
        self.maps[src] = dest
    def get(self, src):
        for rs, re in self.ranges:
            if src >= rs and src <= re:
                return self.maps[rs] + (src - rs)
        return src

def get_key(x):
    m1 = maps[0].get(int(x))
    m2 = maps[1].get(m1)
    m3 = maps[2].get(m2)
    m4 = maps[3].get(m3)
    m5 = maps[4].get(m4)
    m6 = maps[5].get(m5)
    m7 = maps[6].get(m6)
    return m7

def main():
    with open("input.txt") as f:
        content = f.readlines()

    seeds = []
    i = 0
    while i < len(content):
        if content[i].startswith("seeds:"):
            l = content[i].strip()
            for n in l.split(": ")[-1].split():
                seeds.append(int(n))
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
    
    print(get_key(min(seeds, key=get_key)))

if __name__ == "__main__":
    raise SystemExit(main())

import re
from collections import Counter
from copy import deepcopy
from concurrent.futures import ThreadPoolExecutor

class BP:
    def __init__(self, inp: str):
        self.id = int(re.findall(r'Blueprint (\d+):', inp)[0])
        self.ore_robot = int(re.findall(r'Each ore robot costs (\d+) ore.', inp)[0])
        self.clay_robot = int(re.findall(r'Each clay robot costs (\d+) ore.', inp)[0])
        self.obs_robot = tuple(map(
                            int, 
                            re.findall(
                                r'Each obsidian robot costs (\d+) ore and (\d+) clay.',
                                inp
                            )[0]
                        ))
        self.geo_robot = tuple(map(
                            int, 
                            re.findall(
                                r'Each geode robot costs (\d+) ore and (\d+) obsidian.',
                                inp
                            )[0]
                        ))

def rec_geodes(bp: BP, resources, robots, min: int) -> int:
    if min > 24:
        return resources["geo"]
    paths = [resources["geo"]]
    # Begin Build
    if resources["ore"] >= bp.geo_robot[0] and resources["obs"] >= bp.geo_robot[1]:
        res = deepcopy(resources)
        robs = deepcopy(robots)
        res["ore"] -= bp.geo_robot[0]
        res["obs"] -= bp.geo_robot[1]
        for rob, c in robs.items():
            res[rob] += c
        robs["geo"] += 1
        return rec_geodes(bp, res, robs, min+1)
    if resources["ore"] >= bp.obs_robot[0] and resources["clay"] >= bp.obs_robot[1]:
        res = deepcopy(resources)
        robs = deepcopy(robots)
        res["ore"] -= bp.obs_robot[0]
        res["clay"] -= bp.obs_robot[1]
        for rob, c in robs.items():
            res[rob] += c
        robs["obs"] += 1
        paths.append(rec_geodes(bp, res, robs, min+1))
    if resources["ore"] >= bp.clay_robot:
        res = deepcopy(resources)
        robs = deepcopy(robots)
        res["ore"] -= bp.clay_robot
        for rob, c in robs.items():
            res[rob] += c
        robs["clay"] += 1
        paths.append(rec_geodes(bp, res, robs, min+1))
    if resources["ore"] >= bp.ore_robot:
        res = deepcopy(resources)
        robs = deepcopy(robots)
        res["ore"] -= bp.ore_robot
        for rob, c in robs.items():
            res[rob] += c
        robs["ore"] += 1
        paths.append(rec_geodes(bp, res, robs, min+1))

    for rob, c in robots.items():
        resources[rob] += c
    return max(rec_geodes(bp, resources, robots, min+1), *paths)

def _max_geodes(bp: BP):
    resources = Counter({"ore": 0, "clay": 0, "obs": 0, "geo": 0})
    robots = Counter({"ore": 1, "clay": 0, "obs": 0, "geo": 0})
    return bp, rec_geodes(bp, resources, robots, 1)

def thread_comp(content: list[str]):
    bp_quals = []
    futures = []
    with ThreadPoolExecutor(max_workers=len(content)) as executor:
        for l in content:
            bp = BP(l.strip())
            futures.append(executor.submit(_max_geodes, bp))
    while futures:
        f = futures.pop(0)
        if f.done():
            bp, bp_max = f.result()
            bp_quals.append(bp_max*bp.id)
            print(f"Done {bp.id}")
        else:
            futures.append(f)

    print(sum(bp_quals))

def comp(content: list[str]):
    bp_quals = []
    for l in content:
        bp = BP(l.strip())
        _, n = _max_geodes(bp)
        bp_quals.append(n*bp.id)
        print(f"Done {bp.id}")

    print(bp_quals)
    print(sum(bp_quals))

def main():
    with open("input.txt") as f:
        content = f.readlines()

    #thread_comp(content)
    comp(content)

if __name__ == "__main__":
    raise SystemExit(main())


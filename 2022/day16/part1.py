import re
from functools import lru_cache

def rec_max_flow(s, valves, N):
    @lru_cache(maxsize=None)
    def dfs(v, m):
        if m > 30:
            return
        nonlocal flow, flows, seen
        flow += sum(flows)
        if valves[v][0] > 0 and v not in seen:
            flows.append(valves[v][0])
        seen.add(v)
        for u in valves[v][1]:
            dfs(u, m+1)
    flow = 0
    flows = []
    seen = set()
    dfs(s, 1)
    return flow

def max_flow(s, valves, N):
    curr_flow = 0
    flows = []
    seen = set()
    work = [s]
    prev_i = 0
    for i in range(N):
        curr_flow += sum(flows)
        if work:
            v = work.pop(prev_i)
            if valves[v][0] > 0 and v not in seen:
                flows.append(valves[v][0])
            seen.add(v)
            prev_l = len(work)
            for u in valves[v][1]:
                if u not in seen:
                    work.append(u)
            prev_i = prev_l
    return curr_flow

def main() -> int:
    with open("test.txt") as f:
        content = f.readlines()
    valves = {}
    start = None
    for l in content:
        print(re.findall(r'\d+', l))
        l = l.strip().split()
        valve = l[1]
        flow = int(l[4].split("=")[1][:-1])
        conns = [c.strip(',') for c in l[9:]]
        valves[valve] = (flow, conns)
        if start == None:
            start = valve
    print(max_flow(start, valves, 30))

if __name__ == "__main__":
    raise SystemExit(main())


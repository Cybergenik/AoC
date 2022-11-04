from collections import defaultdict

def topo(graph, letters):
    def dfs(u):
        if u not in seen:
            seen.add(u)
            for v in graph[u]:
                dfs(v)
            order.append(u)
    seen = set()
    order = []
    for u in sorted(letters):
        if u not in seen:
            dfs(u)
    return order

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    
    # BKRFTXIUMNGHPLWQVZOYJACDSE
    graph = defaultdict(lambda: [])
    letters = set()
    for l in content:
        inp = l.strip().split()
        v = inp[1]
        u = inp[7]
        letters.add(v)
        letters.add(u)
        graph[u].append(v)
        graph[u].sort()

    topos = topo(graph, letters)
    print("".join(topos))

if __name__ == "__main__":
    raise SystemExit(main())

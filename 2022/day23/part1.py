from collections import defaultdict

def valid_dir(x, y, dir, graph):
    if "N" == dir:
        if graph[(x-1, y)] == '.' and graph[(x-1, y-1)] == '.' and graph[(x-1, y+1)] == '.':
            return (x-1, y)
    if "S" == dir:
        if graph[(x+1, y)] == '.' and graph[(x+1, y-1)] == '.' and graph[(x+1, y+1)] == '.':
            return (x+1, y)
    if "W" == dir:
        if graph[(x, y-1)] == '.' and graph[(x-1, y-1)] == '.' and graph[(x+1, y-1)] == '.':
            return (x, y-1)
    if "E" == dir:
        if graph[(x, y+1)] == '.' and graph[(x-1, y+1)] == '.' and graph[(x+1, y+1)] == '.':
            return (x, y+1)
    return None

def main():
    with open("smol.txt") as f:
        content = f.readlines()
    
    graph = defaultdict(lambda: '.')
    dirs = ["N", "S", "W", "E"]
    for i, l in enumerate(content):
        for j, c in enumerate(l):
            graph[(i,j)] = c

    # Rounds
    for _ in range(10):
        print(f'Round {_}:')
        new_locs = {}
        invalid = set()
        # Compute new positions:
        for k, v in list(graph.items()):
            if v == '#':
                if  valid_dir(*k, "N", graph) and \
                    valid_dir(*k, "S", graph) and \
                    valid_dir(*k, "W", graph) and \
                    valid_dir(*k, "E", graph):
                    print(f'Skipped: {k}')
                    continue
                for dir in dirs:
                    loc = valid_dir(*k, dir, graph)
                    if loc != None:
                        if loc in new_locs.values():
                            invalid.add(loc)
                        else:
                            new_locs[k] = loc
                        break
        # Update map:
        for k, v in new_locs.items():
            if v not in invalid:
                print(f'{k} -> {v}')
                graph[k] = '.'
                graph[v] = '#'
        d = dirs.pop(0)
        dirs.append(d)

    # Find bounds:
    left = None
    right = None
    up = None
    down = None
    for k, v in graph.items():
        if v == "#":
            if left == None or k[1] < left:
                left = k[1]
            if right == None or k[1] > right:
                right = k[1]
            if up == None or k[0] < up:
                up = k[0]
            if down == None or k[0] > down:
                down = k[0]

    print(up, down)
    print(left, right)
    # Count emptys:
    total = 0
    for i in range(up, down+1):
        for j in range(left, right+1):
            if graph[(i,j)] == '.':
                total += 1

    print(total)

if __name__ == "__main__":
    raise SystemExit(main())


def adjacent(x, y):
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)
    yield (x-1, y-1)
    yield (x+1, y+1)
    yield (x-1, y+1)
    yield (x+1, y-1)

def flash(x:int, y:int, octopy) -> int:
    work = [(x,y)]
    flashes = 0
    while work:
        curr = work.pop()
        if octopy[curr] == 0:
            continue
        octopy[curr] = 0
        flashes += 1
        for adj in adjacent(curr[0], curr[1]):
            if adj in octopy and octopy[adj] != 0:
                octopy[adj] += 1
                if octopy[adj] > 9:
                    work.append(adj)
    return flashes

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    octopy = {}
    
    for x, line in enumerate(content):
        line = line.strip()
        for y, num in enumerate(line):
            octopy[(x,y)] = int(num)
    for i in range(1, 1000):
        work = []
        for octo in octopy:
            octopy[octo] += 1
            if octopy[octo] > 9:
                work.append(octo)
        for octo in work:
            flash(octo[0], octo[1], octopy)
        if sum(octopy.values()) == 0:
            print(i)
            break
if __name__ == "__main__":
    raise SystemExit(main())

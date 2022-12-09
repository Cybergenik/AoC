
def new_tail(x, y, zx, zy):
    xdiff = x-zx
    ydiff = y-zy
    if abs(xdiff) == 2:
        if zx > x:
            return zx-1, zy
        else:
            return zx+1, zy
    elif abs(ydiff) == 2:
        if zy > y:
            return zx, zy-1
        else:
            return zx, zy+1
    return x,y

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()   
    visited = set()
    head = (0,0)
    tail = (0,0)
    for l in content:
        inst, c = l.strip().split()
        for _ in range(int(c)):
            if inst == "R":
                head = (head[0]+1, head[1])
            elif inst == "L":
                head = (head[0]-1, head[1])
            elif inst == "U":
                head = (head[0], head[1]+1)
            elif inst == "D":
                head = (head[0], head[1]-1)
            tail = new_tail(*tail, *head)
            visited.add(tail)
    print(len(visited))

if __name__ == "__main__":
    raise SystemExit(main())


def new_tail(x, y, zx, zy):
    xdiff = x-zx
    ydiff = y-zy
    if abs(xdiff) == 2 and abs(ydiff) == 2:
        if zx > x:
            if zy > y:
                return zx-1, zy-1
            else:
                return zx-1, zy+1
        elif zx < x:
            if zy > y:
                return zx+1, zy-1
            else:
                return zx+1, zy+1
    if abs(xdiff) == 2:
        if zx > x:
            return zx-1, zy
        else:
            return zx+1, zy
    if abs(ydiff) == 2:
        if zy > y:
            return zx, zy-1
        else:
            return zx, zy+1
    return x,y

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()   
    visited = set()
    knots = [(0,0) for _ in range(10)]
    for l in content:
        inst, c = l.strip().split()
        for _ in range(int(c)):
            if inst == "R":
                knots[0] = (knots[0][0]+1, knots[0][1])
            elif inst == "L":
                knots[0] = (knots[0][0]-1, knots[0][1])
            elif inst == "U":
                knots[0] = (knots[0][0], knots[0][1]+1)
            elif inst == "D":
                knots[0] = (knots[0][0], knots[0][1]-1)
            for i in range(1, len(knots)):
                knots[i] = new_tail(*knots[i], *knots[i-1])
            visited.add(knots[-1])
    print(len(visited))

if __name__ == "__main__":
    raise SystemExit(main())

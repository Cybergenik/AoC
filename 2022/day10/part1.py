
def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()   

    x = 1
    i = 0
    cycles = []
    ops = []
    cycle = 1

    for l in content:
        inst = l.strip().split()
        if len(inst) == 2:
            ops.append((2, int(inst[1])))
        else:
            ops.append((1, 0))

    for c, op in ops:
        for _ in range(c):
            # during
            if cycle in {20, 60, 100, 140, 180, 220}:
                cycles.append(cycle*x)
               
            cycle += 1
        x += op
            
    print(cycles)
    print(sum(cycles))

if __name__ == "__main__":
    raise SystemExit(main())



def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()   

    x = 1
    ops = []
    cycle = 0

    art = ''

    for l in content:
        inst = l.strip().split()
        if len(inst) == 2:
            ops.append((2, int(inst[1])))
        else:
            ops.append((1, 0))

    curr_row = [' ']*40
    for c, op in ops:
        for _ in range(c):
            # during
            if cycle%40 in {x-1, x, x+1}:
                curr_row[cycle%40] = "#"
            cycle += 1
            if cycle in {40, 80, 120, 160, 200, 240}:
                art += "".join(curr_row)+'\n'
                curr_row = [' ']*40
        x += op
            
    print(art)

if __name__ == "__main__":
    raise SystemExit(main())


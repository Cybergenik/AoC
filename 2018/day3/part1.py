from collections import defaultdict

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    total = 0
    fabric = defaultdict(lambda: 0)
    for l in content:
        patch = l.strip().split()
        j_s, i_s = patch[2].split(",")
        i_s = int(i_s[:-1])
        j_s = int(j_s)
        j_e, i_e = patch[3].split("x")
        j_e = int(j_e)
        i_e = int(i_e)
        print(f'X: {i_s}->{i_e}')
        print(f'Y: {j_s}->{j_e}')
        for i in range(i_s, i_s+i_e):
            for j in range(j_s, j_s+j_e):
                if fabric[(i,j)] == 0:
                    fabric[(i,j)] = 1
                elif fabric[(i,j)] == 1:
                    fabric[(i,j)] = -1
                    total += 1
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

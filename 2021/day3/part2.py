import copy

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()

    c02 = copy.copy(content)
    oxygen = copy.copy(content) 

    for inx in range(12):
        if len(oxygen) > 1:
            ox = [int(x[inx]) for x in oxygen]
            if sum(ox) >= len(ox)/2:
                oxygen = [x for x in oxygen if x[inx] == "1"]
            else:
                oxygen = [x for x in oxygen if x[inx] == "0"]
        
        if len(c02) > 1:
            c = [int(x[inx]) for x in c02]
            if sum(c) >= len(c)/2:
                c02 = [x for x in c02 if x[inx] == "0"]
            else:
                c02 = [x for x in c02 if x[inx] == "1"]

        if len(oxygen) == 1 and len(c02) == 1:
            break
        inx += 1
    print(int(oxygen[0], 2) * int(c02[0], 2))

if __name__ == "__main__":
    raise SystemExit(main())

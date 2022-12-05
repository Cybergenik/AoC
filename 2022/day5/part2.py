def parse(line: str):
    currc = ""
    i = 0
    for c in line:
        i += 1
        if i % 4 == 0:
            yield currc
            currc = ""
        if c != " ":
            currc += c

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()   
    
    stacks = []
    for l in content:
        if l[0] == "[":
            layer = list(parse(l))
            for i,crate in enumerate(layer):
                if crate != '':
                    while i >= len(stacks):
                        stacks.append([])
                    stacks[i].insert(0, crate[1:2])
        elif l[0] == "m":
            layer = l.strip().split()
            amount = int(layer[1])
            from_ = int(layer[3])
            to = int(layer[5])
            vals = stacks[from_-1][-amount:]
            stacks[from_-1] = stacks[from_-1][:-amount]
            for val in vals:
                stacks[to-1].append(val)

    ret = ""
    for i in stacks:
        ret += i[-1]
    print(ret)

if __name__ == "__main__":
    raise SystemExit(main())

from z3 import Int, Optimize, sat

def main():
    with open("input.txt") as f:
        content = f.read()
    
    opt = Optimize()

    for l in content.strip().split("\n"):
        l, r = l.strip().split(": ")
        if l == "humn":
            continue
        if r.isnumeric() == 1:
            opt.add(Int(l) == int(r))
        else:
            n1, op, n2 = tuple(r.split())
            if l == "root":
                opt.add(Int(n1) == Int(n2))
                continue
            if op == '/':
                opt.add(Int(l) == Int(n1) / Int(n2))
            elif op == '*':
                opt.add(Int(l) == Int(n1) * Int(n2))
            elif op == '+':
                opt.add(Int(l) == Int(n1) + Int(n2))
            elif op == '-':
                opt.add(Int(l) == Int(n1) - Int(n2))

    assert opt.check() == sat
    m = opt.model()
    print(m[Int("humn")].as_long())

if __name__ == "__main__":
    raise SystemExit(main())


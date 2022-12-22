
class Num:
    def __init__(self, v: int):
        self.n = v

def main():
    with open("input.txt", "r") as f:
        content = f.readlines()
    
    enc = [] #[Num(int(v)) for v in content]
    for v in content:
        v = int(v)
        enc.append(Num(v))
        if v == 0:
            z = enc[-1]
    mixed = enc[:]
    N = len(enc)
    for v in enc:
        if v.n == 0:
            continue
        i = mixed.index(v)
        ins = (i+v.n)%(N-1)
        val = mixed.pop(i)
        mixed.insert(ins, val)
    
    s = mixed.index(z)
    groove = [mixed[(s+1000)%N].n, mixed[(s+2000)%N].n, mixed[(s+3000)%N].n]
    print(sum(groove))


if __name__ == "__main__":
    raise SystemExit(main())


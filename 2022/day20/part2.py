
def main():
    with open("input.txt", "r") as f:
        content = f.readlines()
    
    key = 811589153
    enc = []
    for i, v in enumerate(content):
        n = (i, int(v)*key) 
        if n[1] == 0:
            z = n
        enc.append(n)
    mixed = enc[:]
    N = len(enc)
    for _ in range(10):
        for v in enc:
            if v[1] == 0:
                continue
            i = mixed.index(v)
            ins = (i+v[1])%(N-1)
            val = mixed.pop(i)
            mixed.insert(ins, val)
    
    s = mixed.index(z)
    groove = [mixed[(s+1000)%N][1], mixed[(s+2000)%N][1], mixed[(s+3000)%N][1]]
    print(sum(groove))


if __name__ == "__main__":
    raise SystemExit(main())


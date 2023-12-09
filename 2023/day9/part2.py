#!/usr/local/bin/python3

def find_next(seq):
    if len(set(seq)) == 1:
        return seq[0]
    vals = []
    for s1, s2 in zip(seq[:-1], seq[1:]):
        vals.append(s2-s1)
    return seq[-1] + find_next(vals)

def main():
    with open("input.txt") as f:
        content = f.readlines()

    total = 0
    for l in content:
        seq = list(map(int, l.strip().split()))
        total += find_next(seq[::-1])
    print(total)

        
if __name__ == "__main__":
    raise SystemExit(main())

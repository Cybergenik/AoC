#!/usr/local/bin/python3

def main():
    with open("input.txt") as f:
        content = f.read()

    locks = []
    keys = []
    for schem in content.strip().split("\n\n"):
        # lock
        if schem[0][0] == "#":
            lock = [0,0,0,0,0]
            for l in schem.split("\n")[1:]:
                for i, c in enumerate(l):
                    if c == "#":
                        lock[i] += 1
            locks.append(lock)
        # lock
        else:
            key = [0,0,0,0,0]
            for l in schem.split("\n")[:-1]:
                for i, c in enumerate(l):
                    if c == "#":
                        key[i] += 1
            keys.append(key)
    total = 0
    for k in keys:
        for l in locks:
            valid = True
            for ki, li in zip(k, l):
                if ki + li > 5:
                    valid = False
                    break
            if valid:
                total += 1
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

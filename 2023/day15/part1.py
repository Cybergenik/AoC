#!/usr/local/bin/python3

def hash(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h

def main():
    with open("input.txt") as f:
        content = f.readlines()
    steps = content[0].strip().split(",")
    print(sum(map(hash, steps)))

if __name__ == "__main__":
    raise SystemExit(main())

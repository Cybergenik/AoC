#!/usr/local/bin/python3

#from functools import lru_cache
from collections import Counter

def main():
    print("Herro there")
    with open("input.txt") as f:
        content = f.readlines()
    
    total = 0
    for l in content:
        id, game = l.strip().split(":")
        id = int(id.split()[-1])
        starting_set = Counter({"red": 0, "green": 0, "blue": 0})
        for g in game.split(";"):
            for c in g.split(","):
                num, color = c.strip().split()
                starting_set[color] = max(starting_set[color], int(num))
        total += starting_set["red"]*starting_set["blue"]*starting_set["green"]
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

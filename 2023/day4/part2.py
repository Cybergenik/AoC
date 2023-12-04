#!/usr/local/bin/python3

from collections import defaultdict

def main():
    with open("input.txt") as f:
        content = f.readlines()

    games = defaultdict(lambda: 0)
    i = 1
    total = 0
    for l in content:
        l = l.strip()
        game = l.split(":")[-1]
        win, cards = game.split("|")
        win = set(map(int, win.strip().split()))
        cards = set(map(int, cards.strip().split()))
        games[i] += 1
        for j in range(i+1, i+len(win.intersection(cards))+1):
            games[j] += games[i]
        total += games[i]
        i += 1
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

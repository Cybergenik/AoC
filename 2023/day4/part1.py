#!/usr/local/bin/python3

def main():
    with open("input.txt") as f:
        content = f.readlines()

    total = 0
    i = 1
    for l in content:
        i += 1
        l = l.strip()
        game = l.split(":")[-1]
        win, cards = game.split("|")
        win = set(map(int, win.strip().split()))
        cards = set(map(int, cards.strip().split()))
        if len(win.intersection(cards)) > 0:
            total += 2**(len(win.intersection(cards))-1)
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

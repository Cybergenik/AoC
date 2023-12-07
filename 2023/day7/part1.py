#!/usr/local/bin/python3

from collections import Counter

class Cards:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        c = Counter(self.cards)
        # Five of a kind
        if len(c) == 1:
            self.type = 7
        # Four of a Kind
        elif c.most_common(1)[0][1] == 4:
            self.type = 6
        # Full House
        elif c.most_common(1)[0][1] == 3 and c.most_common(2)[1][1] == 2:
            self.type = 5
        # Three of a Kind
        elif c.most_common(1)[0][1] == 3:
            self.type = 4
        # Two Pair
        elif c.most_common(1)[0][1] == 2 and c.most_common(2)[1][1] == 2:
            self.type = 3
        # One Pair
        elif c.most_common(1)[0][1] == 2 and c.most_common(2)[1][1] == 1:
            self.type = 2
        # High Card
        else:
            self.type = 1 

    def __lt__(self, o):
        if self.type < o.type:
            return True
        elif self.type > o.type:
            return False
        ordering = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for i in range(len(self.cards)):
            ord1, ord2 = ordering.index(self.cards[i]), ordering.index(o.cards[i])
            if ord1 < ord2:
                return True
            elif ord1 > ord2:
                return False
        return False

def main():
    with open("input.txt") as f:
        content = f.readlines()

    ranks = []
    for l in content:
        l = l.strip()
        cards, bid = l.split()
        ranks.append(Cards(cards, int(bid)))

    total = 0
    ranks = sorted(ranks)
    for i, c in enumerate(ranks):
        total += (i+1)*c.bid
    print(total)
    
if __name__ == "__main__":
    raise SystemExit(main())

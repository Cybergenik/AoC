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

        # Handle 'J' wildcard
        if "J" in c:
            #1. Ignore 5 Jacks
            #2. Four of a kind and Full house both get Five of a kind
            if self.type == 6 or self.type == 5:
                self.type = 7
            #3. Three of a kind always just gets Four of a kind
            elif self.type == 4:
                self.type = 6
            #4. Two Pair gets Four of a kind if Jacks are the pair, else Full House
            elif self.type == 3:
                if c["J"] == 2:
                    self.type = 6
                elif c["J"] == 1:
                    self.type = 5
            #5. One Pair always just becomes Three of a Kind
            elif self.type == 2:
                self.type = 4
            #6. One Jack pairs with any other card
            elif self.type == 1:
                self.type = 2

    def __lt__(self, o):
        if self.type < o.type:
            return True
        elif self.type > o.type:
            return False
        ordering = {c: i for i,c in enumerate(('J', '2', '3', '4', '5', '6',
                                               '7', '8', '9', 'T', 'Q', 'K',
                                               'A'))}
        for i in range(len(self.cards)):
            ord1, ord2 = ordering[self.cards[i]], ordering[o.cards[i]]
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

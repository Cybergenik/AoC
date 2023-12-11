from collections import Counter
print("Herro there")
with open("input.txt") as f:
    content = f.readlines()
total = 0
for l in content:
    id, game = l.strip().split(":")
    id = int(id.split()[-1])
    possible = True
    for g in game.split(";"):
        starting_set = Counter({"red": 12, "green": 13, "blue": 14})
        for c in g.split(","):
            num, color = c.strip().split()
            starting_set[color] -= int(num)
            if starting_set[color] < 0:
                possible = False
                break
        if not possible:
            break
    if possible: 
        total += id
print(total)

import sys

with open("inputs3.txt") as f:
    content = f.readlines()

terrain = [x.strip() for x in content]

def day3(t: list, x: int, y: int) -> int:
    j = 0
    trees = 0
    i = 0
    while i < len(t):
        if j >= len(t[i]):
            j = j % len(t[i])
        if t[i][j] == "#":
            trees += 1
        j += y
        i += x 
    return trees  

# Part 1:
print(day3(terrain, 1, 3))
# Part 2:
print(day3(terrain, 1, 1) * day3(terrain, 1, 3) * day3(terrain, 1, 5) * day3(terrain, 1, 7) * day3(terrain, 2, 1))

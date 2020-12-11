import sys

with open("inputs3.txt") as f:
    content = f.readlines()

terrain = []
for line in content:
    line = line.strip()
    terrain.append([x for x in line])

def day3(t: list, increment: int, slope: int) -> int:
    index = 0
    trees = 0
    i = 0
    while i < len(t):
        if index >= len(t[i]):
            index = index % len(t[i])
        if t[i][index] == "#":
            trees += 1
        index += slope
        i += increment 
    return trees  


#print(day3(terrain, 1, 3))
print(day3(terrain, 1, 1) * day3(terrain, 1, 3) * day3(terrain, 1, 5) * day3(terrain, 1, 7) * day3(terrain, 2, 1))

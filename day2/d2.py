import sys

with open("inputs2.txt") as f:
    content = f.readlines()

passwords = {}

for line in content:
    rule = line.split()
    if rule[1][:-1] not in passwords:
        passwords[rule[1][:-1]] = [[[int(x) for x in rule[0].split("-")]], [rule[2]]]
    else:
        passwords.get(rule[1][:-1])[0].append([int(x) for x in rule[0].split("-")])
        passwords.get(rule[1][:-1])[1].append(rule[2])

def day2(passwords: dict) -> int:
    valid = 0
    for letter in passwords.keys():
        key = passwords.get(letter)
        for j in range(len(key[0])):
            count = 0
            for c in key[1][j]:
                if c == letter:
                   count += 1 
            if count == 0:
                continue
            elif key[0][j][0] <= count <= key[0][j][1]:
                valid += 1
    return valid


def day2_p2(passwords: dict) -> int:
    valid = 0
    for letter in passwords.keys():
        key = passwords.get(letter)
        for j in range(len(key[0])):
            word = key[1][j]
            index1 = (key[0][j][0] - 1)
            index2 = (key[0][j][1] - 1)
            if word[index1] == letter and word[index2] == letter:
                continue
            if word[index1] == letter or word[index2] == letter:
                valid += 1
    return valid
print(day2_p2(passwords))

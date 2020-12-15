import sys

with open("input5.txt") as f:
    content = f.readlines()

tickets = [x.strip() for x in content]


def day5(l: list) -> int:
    for ticket in l:
        

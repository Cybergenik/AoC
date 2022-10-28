import sys
import re

with open("input4.txt") as f:
    content = f.readlines()

def day4(l: list) -> int:
    entries = []
    entry = []
    for line in l:
        if re.search("^\n", line):
            entries.append(entry)
            entry = []
        else:
            e = line.strip().split()
            for i in e:
                entry.append(i)
    if len(entry) != 0:
        entries.append(entry)
    valid = 0
    for i in entries:
        if len(i) <= 6:
            continue
        if len(i) == 8:
            valid += 1
        else:
            val = 1
            for s in i:
                if "cid" in s:
                   val = 0
                   break
            valid += val
    return valid

def day4_part2(l: list) -> int:
    entries = []
    entry = {}
    total = 0
    colors = ['amb','blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for line in l:
        if re.search("^\n", line):
            entries.append(entry)
            entry = {}
        else:
            e = line.strip().split()
            for i in e:
                e = i.split(":")
                entry[e[0]] = e[1]
    if len(entry) != 0:
        entries.append(entry)
    for e in entries:
        if len(e) < 7:
            continue
        if len(e) == 7 and 'cid' in e:
            continue
        valid = 0
        for f in fields:
           val = e[f]
           if f == 'byr':
               if 1920 <= int(val) <= 2002:
                   valid += 1
           elif f == 'iyr':
               if 2010 <= int(val) <= 2020:
                   valid += 1
           elif f == 'eyr':
               if 2020 <= int(val) <= 2030:
                   valid += 1
           elif f == 'hgt':
               if val[-2:] == 'cm':
                   if 150 <= int(val[:-2]) <= 193:
                       valid += 1 
               elif val[-2:] == 'in':
                   if 59 <= int(val[:-2]) <= 76:
                       valid += 1
           elif f == 'hcl':
                if re.search('^#[a-z0-9]{6,6}$', val):
                   valid += 1
           elif f == "ecl":
                if val in colors:
                   valid += 1
           elif f == 'pid':
                if re.search('^[0-9]{9,9}$', val):
                   valid += 1
        if valid == 7:
            total += 1
    return total

print(day4_part2(content))

import sys
from collections import Counter

with open("input5.txt") as f:
    content = f.readlines()

tickets = [x.strip() for x in content]

#def partition(l:set, ) -> list:

def day5(tickets: list) -> int:
    highest = 0
    for ticket in tickets:
        row_upper = 128
        row_lower = 1
        row = 999
        column_upper = 8
        column_lower = 1
        column = 999
        for l in ticket:
            print(f'{row} {column}')
            mrow = row_lower + ((row_upper - row_lower)//2)
            mcolumn = column_lower + ((column_upper - column_lower)//2)
            if (row_upper - row_lower) == 1 and row == 999:
                if l == "F":
                    row = row_lower
                    print("updated")
                elif l == "B":
                    row = row_upper
                    print("updated")
                #print(f"row found {row}")
            elif (column_upper - column_lower) == 1 and column == 999:
                if l == "L":
                    column = column_lower
                elif l == "R":
                    column = column_upper
                #print("column found {column}")
            else:
                if  l == "F":
                    row_upper = mrow
                elif l == "B":
                    row_lower = mrow
                elif l == "L":
                    column_upper = mcolumn
                elif l == "R":
                    column_lower = mcolumn
            print(f'{row_lower}-{row_upper}')
            print(f'{column_lower}-{column_upper}')
        print(f'{row} {column}')
        seat_id = (row * 8) + column
        if seat_id > highest:
            highest = seat_id
    return highest

def derive_row(ticket: str) -> int:
    rows = [x for x in range(0,128)]
    columns = [x for x in range(0,8)]
    for l in ticket:
        
print(day5(["FBFBBFFRLR"]))

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    
    R = "A"
    P = "B"
    S = "C"
    scores = {"X": 1, "Y": 2, "Z": 3}
    total = 0
    for round in content:
        e, m = round.split()
        count = 0
        if e == R:
            if m == "Y":
                count += 6
            elif m == "X":
                count += 3
        elif e == P:
            if m == "Z":
                count += 6
            elif m == "Y":
                count += 3
        elif e == S:
            if m == "X":
                count += 6
            elif m == "Z":
                count += 3
        total += count+scores[m]
    print(total)

    
if __name__ == "__main__":
    raise SystemExit(main())

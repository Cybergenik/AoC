def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()

    t_scores = {"A": 1, "B": 2, "C": 3}
    w_scores = {"A": 2, "B": 3, "C": 1}
    l_scores = {"A": 3, "B": 1, "C": 2}
    total = 0
    for round in content:
        e, m = round.split()
        count = 0
        if m == "X":
            count += l_scores[e]
        if m == "Y":
            count += 3
            count += t_scores[e]
        elif m == "Z":
            count += 6
            count += w_scores[e]
        total += count
    print(total)

    
if __name__ == "__main__":
    raise SystemExit(main())

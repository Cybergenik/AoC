
def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()

    gamma = ""
    er = ""
    for indx in range(12):
        total = [int(x[indx]) for x in content]
        if sum(total) >= len(total)/2:
            gamma += "1"
            er += "0"
        else:
            gamma += "0"
            er += "1"
        
    print(int(gamma, 2) * int(er, 2))

if __name__ == "__main__":
    raise SystemExit(main())


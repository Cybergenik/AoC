
def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    caves: list[list[int]] = []
    for line in content:
        caves.append([int(x) for x in line.strip()])
    total = 0
    for i in range(len(caves)):
        for j in range(len(caves[i])):
            if i > 0:
                if caves[i][j] >= caves[i-1][j]:
                    continue
            if i < len(caves)-1:
                if caves[i][j] >= caves[i+1][j]:
                    continue
            if j > 0:
                if caves[i][j] >= caves[i][j-1]:
                    continue
            if j < len(caves[i])-1:
                if caves[i][j] >= caves[i][j+1]:
                    continue
            total += caves[i][j] + 1
    print(total)
            
            
                

if __name__ == "__main__":
    raise SystemExit(main())

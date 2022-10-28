def find_basin(xy: tuple[int, int], caves: list[list[int]]) -> int:
    seen: set[tuple[int,int]] = set()
    near = [xy]
    while near:
        curr = near.pop()
        seen.add(curr)
        if curr[0] != 0:
            if caves[curr[0]-1][curr[1]] != 9 and (curr[0]-1, curr[1]) not in seen:
                near.append((curr[0]-1, curr[1]))
        if curr[0] != len(caves)-1:
            if caves[curr[0]+1][curr[1]] != 9 and (curr[0]+1, curr[1]) not in seen:
                near.append((curr[0]+1, curr[1]))
        if curr[1] != 0:
            if caves[curr[0]][curr[1]-1] != 9 and (curr[0], curr[1]-1) not in seen:
                near.append((curr[0], curr[1]-1))
        if curr[1] != len(caves[curr[0]])-1:
            if caves[curr[0]][curr[1]+1] != 9 and (curr[0],curr[1]+1) not in seen:
                near.append((curr[0], curr[1]+1))
    return len(seen)
   

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    caves: list[list[int]] = []
    for line in content:
        caves.append([int(x) for x in line.strip()])
    
    basins = []
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
            basins.append(find_basin((i, j), caves))
    basins.sort()

    print(basins[-1] * basins[-2] * basins[-3])

if __name__ == "__main__":
    raise SystemExit(main())

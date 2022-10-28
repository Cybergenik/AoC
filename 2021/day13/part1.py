from os import EX_NOTFOUND


def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    
    maxX = 0
    maxY = 0
    paper = {}
    i = 0
    while content[i] != '\n':
        y,x = content[i].strip().split(',')
        paper[int(x),int(y)] = "#"
    i += 1
    while content[i]:
        


if __name__ == "__main__":
    raise SystemExit(main())
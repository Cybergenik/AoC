
def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()   
    content = content[0]
    for c in range(14, len(content)):
        if len(set(content[c-14:c])) == 14:
            print(c)
            break

if __name__ == "__main__":
    raise SystemExit(main())

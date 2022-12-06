
def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()   
    content = content[0]
    for c in range(4, len(content)):
        if len(set(content[c-4:c])) == 4:
            print(c)
            break
    
if __name__ == "__main__":
    raise SystemExit(main())

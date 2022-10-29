
def reducePolymer(s: str):
    polymer = list(s)
    i = 1
    while i < len(polymer)-1:
        if polymer[i] != polymer[i+1] and polymer[i].lower() == polymer[i+1].lower():
            polymer.pop(i)
            polymer.pop(i)
        elif polymer[i] != polymer[i-1] and polymer[i].lower() == polymer[i-1].lower():
            i -= 1
            polymer.pop(i)
            polymer.pop(i)
        else:
            i += 1
    return "".join(polymer)

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()

    print(len(reducePolymer(content[0].strip())))

if __name__ == "__main__":
    raise SystemExit(main())

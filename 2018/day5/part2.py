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
    
    content = content[0].strip()
    letters = set()
    smallest = None
    for c in content:
        if c.islower():
            letters.add(c)
    for c in letters:
        new_c = content.replace(c, "").replace(c.upper(), "")
        curr = len(reducePolymer(new_c))
        if not smallest or curr < smallest:
            smallest = curr

    print(smallest)

if __name__ == "__main__":
    raise SystemExit(main())

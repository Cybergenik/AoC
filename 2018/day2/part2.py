from collections import Counter

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()

    for i in range(len(content)-1):
        for j in range(i+1, len(content)):
            diff = []
            for indx, (l, r) in enumerate(zip(content[i].strip(), content[j].strip())):
                if l != r:
                    diff.append((indx,l))
            if len(diff) == 1:
                correct_box = ""
                for c in enumerate(content[i].strip()):
                    if c not in diff:
                        correct_box += c[1]
                print(correct_box)
                return

if __name__ == "__main__":
    raise SystemExit(main())

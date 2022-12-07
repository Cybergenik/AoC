from collections import defaultdict

class FS:
    def __init__(self, content):
        self.fs = defaultdict(lambda: 0)
        self.loc = None
        for l in content:
            l = l.strip().split()
            if l[0] == "$":
                if l[1] == "cd" and l[2] != "..":
                    if not self.loc:
                        self.loc = (l[2],)
                    else:
                        self.loc = (*self.loc, l[2])
                elif l[1] == "cd" and l[2] == "..":
                    self.loc = self.loc[:-1]
            elif l[0].isnumeric():
                curr_l = self.loc
                while curr_l:
                    self.fs[curr_l] += int(l[0])
                    curr_l = curr_l[:-1]
    
    def find_dirs(self):
        total = 0
        for dir, data in self.fs.items():
            if data <= 100000:
                total += data
        return total

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()   

    fs = FS(content)
    print(fs.find_dirs())
    
if __name__ == "__main__":
    raise SystemExit(main())

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
    
    def min_dir(self):
        min_dir = None
        free = 70000000 - (self.fs[("/",)])
        for dir, data in self.fs.items():
            if not min_dir or (free+data >= 30000000 and data < min_dir):
                min_dir = data
        return min_dir

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()   

    fs = FS(content)
    print(fs.min_dir())
    
if __name__ == "__main__":
    raise SystemExit(main())

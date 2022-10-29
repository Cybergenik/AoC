from collections import defaultdict, Counter

class Log:
    def __init__(self, month, day, hour, min, log):
        self.month = month
        self.day = day
        self.hour = hour
        self.min = min
        self.log = log
        self.guard = None
        self.mark = None
        if "#" in log:
            self.guard = int(log.split()[1][1:])
        elif "falls" in log:
            self.mark = "S"
        else:
            self.mark = "W"

    def __lt__(self, other):
        if self.month < other.month:
            return True
        if self.month > other.month:
            return False
        if self.day < other.day:
            return True
        if self.day > other.day:
            return False
        if self.hour < other.hour:
            return True
        if self.hour > other.hour:
            return False
        if self.min < other.min:
            return True
        if self.min > other.min:
            return False
        return False

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()
    
    logs = [] 
    for l in content:
        l = l.strip()
        md, hm, log = l.split(" ", 2)
        month, day = md.split("-")[1:]
        hour, min = hm[:-1].split(":")
        logs.append(Log(int(month), int(day), int(hour), int(min), log))
    logs.sort()
    minutes = defaultdict(lambda: Counter())
    curr = None
    s = None
    e = None
    for log in logs:
        if log.guard:
            curr = log.guard
        elif log.mark == "S":
            s = log
        elif log.mark == "W":
            e = log
            for m in range(s.min, e.min):
                minutes[m][curr] += 1
    s_guard = max(minutes.items(), key= lambda x: x[1].most_common(1)[0][1])
    top_min = s_guard[0]
    top_guard = s_guard[1].most_common(1)[0][0]
    print(top_guard * top_min)

if __name__ == "__main__":
    raise SystemExit(main())

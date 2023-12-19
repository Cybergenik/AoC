#!/usr/local/bin/python3

from collections import defaultdict

class Workflow:
    def __init__(self):
        self.wfs = defaultdict(lambda: [])

    def add(self, name, rules):
        for rule in rules:
            if len(rule) > 1:
                r = (rule[1].replace(rule[0], f"part['{rule[0]}']"), rule[2])
            else:
                r = ("True", rule[0])
            self.wfs[name].append(r)

    #{x: 1, m: 2, a: 3, s: 4}
    def eval_part(self, part):
        curr = "in"
        while curr not in "AR":
            for rule, dest in self.wfs[curr]:
                if eval(rule):
                    curr = dest
                    break
        return dest == "A"

def main():
    with open("input.txt") as f:
        content = f.readlines()

    total = 0
    WF = Workflow()
    for l in content:
        l = l.strip()
        if l == "": continue
        if not l.startswith("{"):
            name, wf = l.split("{")
            rules = []
            for rule in wf[:-1].split(","):
                if ":" in rule:
                    rule, dest = rule.split(":")
                    rules.append((rule[0], rule, dest))
                else:
                    rules.append((rule,))
            WF.add(name, rules)
        else:
            part = {}
            for r in l[1:-1].split(","):
                x,n = r.split("=")
                part[x] = int(n)
            if WF.eval_part(part):
                total += sum(part.values())
    print(total)
                
if __name__ == "__main__":
    raise SystemExit(main())

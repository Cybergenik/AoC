#!/usr/local/bin/python3

from collections import defaultdict
from copy import copy
import re

class Workflow:
    def __init__(self):
        self.wfs = defaultdict(lambda: [])

    def add(self, name, rules):
        for rule in rules:
            if len(rule) > 1:
                op, n, _ = re.split(r"(\d+)", rule[1][1:])
                r = (rule[0], op, int(n), rule[2])
            else:
                r = (None, None, None, rule[0])
            self.wfs[name].append(r)

    def __str__(self):
        s = ""
        for k, v in self.wfs.items():
            s += f'{k}: {v}\n'
        return s

    #{x: 1, m: 2, a: 3, s: 4}
    def eval_all_paths(self, wf, fit_set):
        if wf == "A":
            combos = 1
            print(fit_set)
            for s, e in fit_set.values():
                combos *= (e-s+1)
            return combos
        if wf == "R":
            return 0
        total_combos = 0
        for name, op, num, dest in self.wfs[wf]:
            if op == "<":
                s, e = fit_set[name]
                if num < e and num > s:
                    fs = copy(fit_set)
                    fs[name] = (s, num-1)
                    fit_set[name] = (num, e)
                    total_combos += self.eval_all_paths(dest, fs)
            elif op == ">":
                s, e = fit_set[name]
                if num < e and num > s:
                    fs = copy(fit_set)
                    fs[name] = (num+1, e)
                    fit_set[name] = (s, num)
                    total_combos += self.eval_all_paths(dest, fs)
            else:
                total_combos += self.eval_all_paths(dest, fit_set)
        return total_combos

    def find_all(self):
        # x, m, a, s
        fit_set = {
                "x": (1, 4000),
                "m": (1, 4000),
                "a": (1, 4000),
                "s": (1, 4000),
        }

        return self.eval_all_paths("in", fit_set)

def main():
    with open("input.txt") as f:
        content = f.readlines()

    total = 0
    WF = Workflow()
    for l in content:
        l = l.strip()
        if l == "": break
        name, wf = l.split("{")
        rules = []
        for rule in wf[:-1].split(","):
            if ":" in rule:
                rule, dest = rule.split(":")
                rules.append((rule[0], rule, dest))
            else:
                rules.append((rule,))
        WF.add(name, rules)
    print(WF.find_all())
                
if __name__ == "__main__":
    raise SystemExit(main())

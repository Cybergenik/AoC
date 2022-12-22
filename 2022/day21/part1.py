
def resolve_rules(rules, r):
    if type(rules[r]) == int:
        return rules[r]
    else:
        #print(rules[r])
        if rules[r][1] == '/':
            return resolve_rules(rules, rules[r][0]) / resolve_rules(rules, rules[r][2])
        elif rules[r][1] == '*':
            return resolve_rules(rules, rules[r][0]) * resolve_rules(rules, rules[r][2])
        elif rules[r][1] == '+':
            return resolve_rules(rules, rules[r][0]) + resolve_rules(rules, rules[r][2])
        elif rules[r][1] == '-':
            return resolve_rules(rules, rules[r][0]) - resolve_rules(rules, rules[r][2])

def main():
    with open("input.txt") as f:
        content = f.read()
    
    rules = {}
    for l in content.strip().split("\n"):
        l, r = l.strip().split(": ")
        if r.isnumeric() == 1:
            rules[l] = int(r)
        else:
            rules[l] = tuple(r.split())

    print(resolve_rules(rules, "root"))

if __name__ == "__main__":
    raise SystemExit(main())


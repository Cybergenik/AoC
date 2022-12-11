from math import lcm
from tqdm import tqdm

class Monkey:
    def __init__(self, items, op, val, div, true_m, false_m):
        self.items = items
        self.op = op
        self.val = val
        self.div = div
        self.true_m = true_m
        self.false_m = false_m
    def round(self, com_mul) -> int:
        while self.items:
            item = self.items.pop(0)
            if self.val == "old":
                val = item
            else:
                val = int(self.val)
            if self.op == "*":
                item *= val
            elif self.op == "+":
                item += val
            item = item%com_mul
            if item%self.div == 0:
                yield (self.true_m, item)
            else:
                yield (self.false_m, item)

def main() -> int:
    with open("input.txt") as f:
        content = f.read()

    monkeys = []
    monkey_business = [0]*8
    content = content.split("\n\n")
    for i, monkey in enumerate(content):
        lines = monkey.split("\n")

        items = list(map(int, lines[1].replace(",", "").split()[2:]))
        op, val = lines[2].split()[4:]
        div = int(lines[3].split()[-1])
        true_m = int(lines[4].split()[-1])
        false_m = int(lines[5].split()[-1])

        monkeys.append(Monkey(items, op, val, div, true_m, false_m))

    com_mul = lcm(*[m.div for m in monkeys])
    for _ in tqdm(range(10_000)):
        for im, m in enumerate(monkeys):
            for i, item in m.round(com_mul):
                monkey_business[im] += 1
                monkeys[i].items.append(item)
    monkey_business = sorted(monkey_business, reverse=True)
    print(monkey_business[0] * monkey_business[1])

if __name__ == "__main__":
    raise SystemExit(main())


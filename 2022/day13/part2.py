import ast 

def compare(l:list, r:list):
    for i in range(min(len(l), len(r))):
        # base:
        if isinstance(l[i], int) and isinstance(r[i], int):
            if l[i] < r[i]:
                return 1
            elif l[i] > r[i]:
                return -1
        # rec:
        else:
            left = l[i]
            right = r[i]
            if isinstance(l[i], int):
                left = [left]
            elif isinstance(r[i], int):
                right = [right]
            rec_cmp = compare(left, right)
            if rec_cmp != 0:
                return rec_cmp
    if len(l) < len(r): 
        return 1
    elif len(l) > len(r):
        return -1
    else:
        return 0

class Packet:
    def __init__(self, dat: list):
        self.packet = dat

    def __lt__(self, other):
        if compare(self.packet, other.packet) >= 0:
            return True
        else:
            return False
    def __eq__(self, other):
        return compare(self.packet, other.packet) == 0

def main():
    with open("input.txt") as f:
        content = f.read()

    packets = [Packet([[2]]), Packet([[6]])]
    pairs = content.split("\n\n")
    for i, pair in enumerate(pairs):
        l, r = pair.strip('\n').split("\n")
        packets.append(Packet(ast.literal_eval(l)))
        packets.append(Packet(ast.literal_eval(r)))
    
    packets = sorted(packets)
    key = 0
    for i in range(len(packets)):
        if packets[i] == Packet([[2]]):
            key += i+1
        elif packets[i] == Packet([[6]]):
            key *= i+1
    print(key)
if __name__ == "__main__":
    raise SystemExit(main())


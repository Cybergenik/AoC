#!/usr/local/bin/python3

from collections import Counter

def price_n(num, n):
    secret = num
    prices = [num%10]
    for _ in range(n):
        secret ^= secret*64
        secret %= 16777216
        secret ^= secret//32
        secret %= 16777216
        secret ^= secret*2048
        secret %= 16777216
        prices.append(secret % 10)
    return prices

def max_prof(m_prices):
    pdiffs = []
    for prices in m_prices:
        diffs = []
        for v1, v2 in zip(prices[:-1], prices[1:]):
            diffs.append(v2-v1)
        pdiffs.append(diffs)
    c = Counter()
    seens = [set() for _ in range(len(pdiffs))]
    for i in range(len(pdiffs[0])-4):
        for j, diffs in enumerate(pdiffs):
            seq = tuple(diffs[i:i+4])
            if seq not in seens[j]:
                seens[j].add(seq)
                c[seq] += m_prices[j][i+4]
    return c.most_common(1)[0][1]

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    nums = [int(l.strip()) for l in content]
    print(max_prof([price_n(n, 2000) for n in nums]))
    
if __name__ == "__main__":
    raise SystemExit(main())

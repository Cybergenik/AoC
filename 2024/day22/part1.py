#!/usr/local/bin/python3

from functools import cache

@cache
def secret_n(num, n):
    secret = num
    for _ in range(n):
        secret ^= secret*64
        secret %= 16777216
        secret ^= secret//32
        secret %= 16777216
        secret ^= secret*2048
        secret %= 16777216
    return secret

def main():
    with open("input.txt") as f:
        content = f.readlines()
    
    nums = [int(l.strip()) for l in content]
    total = 0
    for n in nums:
        total += secret_n(n, 2000)
    print(total)

    
if __name__ == "__main__":
    raise SystemExit(main())

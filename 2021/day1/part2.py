
def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()

    nums = [int(num) for num in content]
    total = 0
    start = 3
    end = 6
    prev = sum(nums[0:3])
    while end <= len(nums):
        curr = sum(nums[start:end])
        if curr > prev:
            total += 1
        prev = curr
        start += 1
        end += 1
    print(total)

if __name__ == "__main__":
    raise SystemExit(main())

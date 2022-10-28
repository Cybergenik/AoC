
def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()

    nums = [int(num) for num in content]
    total_increase = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            total_increase += 1
    print(total_increase)

if __name__ == "__main__":
    raise SystemExit(main())

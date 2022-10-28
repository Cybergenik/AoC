from collections import Counter 

def main() -> int:
    with open("input.txt") as f:
        content = f.readlines()

    nums = Counter([int(x) for x in content[0].split(",")])
    for _ in range(80):
        nums2 = Counter({8: nums[0], 6: nums[0]}) 
        for k, v in nums.items():
            if k > 0:
                nums2[k-1] += v
        nums = nums2 
    print(sum(nums.values()))

if __name__ == "__main__":
    raise SystemExit(main())
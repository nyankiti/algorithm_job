from sys import stdin


def main():
    nums = list(map(int, stdin.readline().split()))
    b = nums[1]
    nums.sort()

    if nums[0] <= nums[1] and nums[1] <= nums[2] and nums[1] == b:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()

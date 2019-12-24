def calc_fuel(num):
    if num <= 0:
        return 0
    else:
        curr = num // 3 - 2
        if curr <= 0:
            return 0
        else:
            return curr + calc_fuel(curr)


if __name__ == "__main__":
    nums = []
    with open("../input/day1input") as f:
        for line in f:
            num = int(line.rstrip())
            nums.append(num)

    result = 0
    for num in nums:
        result += calc_fuel(num)

    print(result)

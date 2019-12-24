WIDTH, HEIGHT = 25, 6
SIZE = WIDTH * HEIGHT


def get_fewest(nums):
    min_num0 = 2 ** 31 - 1
    min_one, min_two = 0, 0
    for i in range(0, len(nums), SIZE):
        curr = nums[i: i + SIZE]
        num0, num1, num2 = 0, 0, 0
        for digit in curr:
            if digit == "0":
                num0 += 1
            if digit == "1":
                num1 += 1
            if digit == "2":
                num2 += 1
        if num0 < min_num0:
            min_num0 = num0
            min_one, min_two = num1, num2
    return min_one, min_two


if __name__ == "__main__":
    with open("../input/day8input") as f:
        for line in f:
            nums = str(line).rstrip()
    num1, num2 = get_fewest(nums)
    print(num1 * num2)

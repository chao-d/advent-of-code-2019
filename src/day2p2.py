TARGET = 19690720


def get_result(nums):
    curr = nums[:]
    for i in range(100):
        for j in range(100):
            nums = curr[:]
            nums[1], nums[2] = i, j
            print(calc(nums))
            if calc(nums) == TARGET:
                print(i, j)
                print("result = " + str(100 * i + j))
                return


def calc(nums):
    length = len(nums)
    for i in range(0, length, 4):
        if nums[i] == 99 or (nums[i] != 1 and nums[i] != 2):
            break
        first_num = nums[nums[i + 1]]
        sec_num = nums[nums[i + 2]]
        if nums[i] == 1:
            nums[nums[i + 3]] = first_num + sec_num
        else:
            nums[nums[i + 3]] = first_num * sec_num

    return nums[0]


if __name__ == "__main__":
    nums = []
    with open("../input/day2input") as f:
        for line in f:
            nums = [int(num) for num in line.split(",")]

    get_result(nums)

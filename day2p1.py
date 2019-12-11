def preprocess():
    nums[1] = 12
    nums[2] = 2


def calc():
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
    with open("./day2input") as f:
        for line in f:
            nums = [int(num) for num in line.split(",")]
    preprocess()
    print(calc())

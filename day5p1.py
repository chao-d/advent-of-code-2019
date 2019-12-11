INPUT = 1


def calc(nums):
    idx = 0
    while idx < len(nums):
        num = str(nums[idx])
        paramodes = []
        if len(num) <= 2:
            if int(num) == 99:
                return
            opcode = int(num[-1])
        else:
            opcode = int(num[-2:])
            if int(num) == 99:
                return
            for i in range(-3, -len(num) - 1, -1):
                paramodes.append(int(num[i]))

        idx = run_tests(nums, idx, paramodes, opcode)


def run_tests(nums, idx, paramodes, opcode):
    if opcode < 3:
        first_num = nums[nums[idx + 1]] \
            if len(paramodes) < 1 or paramodes[0] == 0 else nums[idx + 1]
        sec_num = nums[nums[idx + 2]] \
            if len(paramodes) < 2 or paramodes[1] == 0 else nums[idx + 2]
        if opcode == 1:
            nums[nums[idx + 3]] = first_num + sec_num
        else:
            nums[nums[idx + 3]] = first_num * sec_num
        return idx + 4
    else:
        if opcode == 3:
            nums[nums[idx + 1]] = INPUT
        else:
            val = nums[nums[idx + 1]] \
                if len(paramodes) < 1 or paramodes[0] == 0 else nums[idx + 1]
            print(val)
        return idx + 2


if __name__ == "__main__":
    nums = []
    with open("./day5input") as f:
        for line in f:
            nums = [int(num) for num in line.split(",")]

    calc(nums)

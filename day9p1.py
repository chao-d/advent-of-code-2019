INPUT = 1


def calc(nums):
    idx = 0
    base = [0]
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

        idx = run_tests(nums, idx, paramodes, opcode, base)


def expand_nums(nums, pos):
    for i in range(2 * pos):
        nums.append(0)


def run_tests(nums, idx, paramodes, opcode, base):
    if opcode == 3 or opcode == 4 or opcode == 9:
        pos = nums[idx + 1] \
                       if len(paramodes) < 1 or paramodes[0] == 0 \
                       else nums[idx + 1] + base[0]
        if pos > len(nums):
            expand_nums(nums, pos)
        if opcode == 9:
            if len(paramodes) < 1 or paramodes[0] != 1:
                base[0] += nums[pos]
            else:
                base[0] += nums[idx + 1]
        elif opcode == 3:
            nums[pos] = INPUT
        else:
            if len(paramodes) < 1 or paramodes[0] != 1:
                val = nums[pos]
            else:
                val = nums[idx + 1]
            print(val)
        return idx + 2
    else:
        pos1 = nums[idx + 1] if len(paramodes) < 1 or paramodes[0] == 0 \
            else nums[idx + 1] + base[0]
        pos2 = nums[idx + 2] if len(paramodes) < 2 or paramodes[1] == 0 \
            else nums[idx + 2] + base[0]
        if max(pos1, pos2) > len(nums):
            expand_nums(nums, max(pos1, pos2))
        first_num, sec_num = 0, 0
        if len(paramodes) < 1 or paramodes[0] != 1:
            first_num = nums[pos1]
        else:
            first_num = nums[idx + 1]
        if len(paramodes) < 2 or paramodes[1] != 1:
            sec_num = nums[pos2]
        else:
            sec_num = nums[idx + 2]

        if 5 <= opcode < 7:
            if opcode == 5:
                return idx + 3 if first_num == 0 else sec_num
            else:
                return idx + 3 if first_num != 0 else sec_num
        else:
            pos3 = nums[idx + 3] if len(paramodes) < 3 or paramodes[2] == 0 \
                    else nums[idx + 3] + base[0]
            if pos3 > len(nums):
                expand_nums(nums, pos3)
            if opcode < 3:
                if opcode == 1:
                    nums[pos3] = first_num + sec_num
                else:
                    nums[pos3] = first_num * sec_num
                return idx + 4
            else:
                if opcode == 7:
                    nums[pos3] = 1 if first_num < sec_num else 0
                else:
                    nums[pos3] = 1 if first_num == sec_num else 0
                return idx + 4


if __name__ == "__main__":
    nums = []
    with open("./day9input") as f:
        for line in f:
            nums = [int(num) for num in line.split(",")]
    calc(nums)

from itertools import permutations


PHASES = [0, 1, 2, 3, 4]


def calc(inputs, nums):
    idx = 0
    val = 0
    input_idx = 0
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

        idx, val = run_tests(inputs[input_idx], nums, idx, paramodes, opcode)
        if opcode == 4:
            return val
        if opcode == 3:
            input_idx += 1
            input_idx = min(input_idx, 1)


def run_tests(input_val, nums, idx, paramodes, opcode):
    output = -2 ** 31
    if opcode == 3 or opcode == 4:
        if opcode == 3:
            nums[nums[idx + 1]] = input_val
        else:
            val = nums[nums[idx + 1]] \
                if len(paramodes) < 1 or paramodes[0] == 0 else nums[idx + 1]
            output = val
        return idx + 2, output
    else:
        first_num = nums[nums[idx + 1]] \
            if len(paramodes) < 1 or paramodes[0] == 0 else nums[idx + 1]
        sec_num = nums[nums[idx + 2]] \
            if len(paramodes) < 2 or paramodes[1] == 0 else nums[idx + 2]
        if opcode < 3:
            if opcode == 1:
                nums[nums[idx + 3]] = first_num + sec_num
            else:
                nums[nums[idx + 3]] = first_num * sec_num
            return idx + 4, output
        elif opcode < 7:
            if opcode == 5:
                return idx + 3 if first_num == 0 else sec_num, output
            else:
                return idx + 3 if first_num != 0 else sec_num, output
        else:
            if opcode == 7:
                nums[nums[idx + 3]] = 1 if first_num < sec_num else 0
            else:
                nums[nums[idx + 3]] = 1 if first_num == sec_num else 0
            return idx + 4, output


def gen_perm(nums):
    return [perm for perm in permutations(nums, len(nums))]


if __name__ == "__main__":
    nums = []
    with open("./day7input") as f:
        for line in f:
            nums = [int(num) for num in line.split(",")]

    max_val = -2 ** 63
    perms = gen_perm(PHASES)
    for perm in perms:
        val = 0
        for i in range(len(perm)):
            val = calc([perm[i], val], nums)
        max_val = max(max_val, val)

    print(max_val)

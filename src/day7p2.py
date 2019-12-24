from itertools import permutations


PHASES = [5, 6, 7, 8, 9]


def calc(instr_ptr, idx, inputs, nums, is_first_round):
    val = 0
    input_idx = 0 if is_first_round else -1
    while instr_ptr[idx] < len(nums):
        num = str(nums[instr_ptr[idx]])
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

        instr_ptr[idx], val = run_tests(inputs[idx][input_idx], nums,
                                        instr_ptr, idx, paramodes, opcode)
        if opcode == 4:
            return val
        if opcode == 3 and is_first_round:
            is_first_round = False
            input_idx = -1
    return


def run_tests(input_val, nums, instr_ptr, idx, paramodes, opcode):
    output = -2 ** 31
    if opcode == 3 or opcode == 4:
        if opcode == 3:
            nums[nums[instr_ptr[idx] + 1]] = input_val
        else:
            val = nums[nums[instr_ptr[idx] + 1]] \
                if len(paramodes) < 1 or paramodes[0] == 0 \
                else nums[instr_ptr[idx] + 1]
            output = val
        return instr_ptr[idx] + 2, output
    else:
        first_num = nums[nums[instr_ptr[idx] + 1]] \
            if len(paramodes) < 1 or paramodes[0] == 0 \
            else nums[instr_ptr[idx] + 1]
        sec_num = nums[nums[instr_ptr[idx] + 2]] \
            if len(paramodes) < 2 or paramodes[1] == 0 \
            else nums[instr_ptr[idx] + 2]
        if opcode < 3:
            if opcode == 1:
                nums[nums[instr_ptr[idx] + 3]] = first_num + sec_num
            else:
                nums[nums[instr_ptr[idx] + 3]] = first_num * sec_num
            return instr_ptr[idx] + 4, output
        elif opcode < 7:
            if opcode == 5:
                return instr_ptr[idx] + 3 if first_num == 0 \
                                          else sec_num, output
            else:
                return instr_ptr[idx] + 3 if first_num != 0 \
                                          else sec_num, output
        else:
            if opcode == 7:
                nums[nums[instr_ptr[idx] + 3]] = 1 \
                    if first_num < sec_num else 0
            else:
                nums[nums[instr_ptr[idx] + 3]] = 1 \
                    if first_num == sec_num else 0
            return instr_ptr[idx] + 4, output


def gen_perm(nums):
    return [perm for perm in permutations(nums, len(nums))]


if __name__ == "__main__":
    nums = []
    with open("../input/day7input") as f:
        for line in f:
            nums = [int(num) for num in line.split(",")]

    max_val = -2 ** 63
    perms = gen_perm(PHASES)
    original = nums[:]
    for perm in perms:
        instr_ptr = [0, 0, 0, 0, 0]
        val = 0
        prev_val = 0
        i = 0
        nums = original[:]
        inputs = [[num] for num in perm]
        inputs[0].append(0)
        while True:
            val = calc(instr_ptr, i % len(perm), inputs,
                       nums, i < len(perm))
            if val is None:
                break
            else:
                inputs[(i + 1) % len(perm)].append(val)
            i += 1
        for num in inputs[0]:
            max_val = max(max_val, num)

        print("max_val = " + str(max_val) + "\n")

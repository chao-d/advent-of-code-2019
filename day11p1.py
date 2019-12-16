def calc(nums, ip, ipt, output):
    base = [0]
    while ip[0] < len(nums):
        num = str(nums[ip[0]])
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

        run_tests(nums, ip, paramodes, opcode, base, ipt, output)
        if len(output) == 2:
            print("OUTPUT = " + str(output))
            return


def expand_nums(nums, pos):
    for i in range(pos + 1):
        nums.append(0)


def run_tests(nums, ip, paramodes, opcode, base, ipt, output):
    if opcode == 3 or opcode == 4 or opcode == 9:
        pos = nums[ip[0] + 1] \
                       if len(paramodes) < 1 or paramodes[0] == 0 \
                       else nums[ip[0] + 1] + base[0]
        if pos > len(nums):
            expand_nums(nums, pos)
        if opcode == 9:
            if len(paramodes) < 1 or paramodes[0] != 1:
                base[0] += nums[pos]
            else:
                base[0] += nums[ip[0] + 1]
        elif opcode == 3:
            nums[pos] = ipt
            ip[0] += 2
        else:
            if len(paramodes) < 1 or paramodes[0] != 1:
                val = nums[pos]
            else:
                val = nums[ip[0] + 1]
            ip[0] += 2
            if val is not None:
                output.append(int(val))
    else:
        pos1 = nums[ip[0] + 1] if len(paramodes) < 1 or paramodes[0] == 0 \
            else nums[ip[0] + 1] + base[0]
        pos2 = nums[ip[0] + 2] if len(paramodes) < 2 or paramodes[1] == 0 \
            else nums[ip[0] + 2] + base[0]
        if max(pos1, pos2) > len(nums):
            expand_nums(nums, max(pos1, pos2))
        first_num, sec_num = 0, 0
        if len(paramodes) < 1 or paramodes[0] != 1:
            first_num = nums[pos1]
        else:
            first_num = nums[ip[0] + 1]
        if len(paramodes) < 2 or paramodes[1] != 1:
            sec_num = nums[pos2]
        else:
            sec_num = nums[ip[0] + 2]

        if 5 <= opcode < 7:
            if opcode == 5:
                ip[0] = ip[0] + 3 if first_num == 0 else sec_num
            else:
                ip[0] = ip[0] + 3 if first_num != 0 else sec_num
        else:
            pos3 = nums[ip[0] + 3] if len(paramodes) < 3 or paramodes[2] == 0 \
                    else nums[ip[0] + 3] + base[0]
            if pos3 > len(nums):
                expand_nums(nums, pos3)
            if opcode < 3:
                if opcode == 1:
                    nums[pos3] = first_num + sec_num
                else:
                    nums[pos3] = first_num * sec_num
            else:
                if opcode == 7:
                    nums[pos3] = 1 if first_num < sec_num else 0
                else:
                    nums[pos3] = 1 if first_num == sec_num else 0
            ip[0] += 4


def run(nums):
    ip = [0]
    ipt = 1

    matrix = [["." for _ in range(1000)] for _ in range(1000)]
    curr = [500, 500]
    direction = ["UP"]
    count = 0

    visited = set()

    while True:
        output = []
        if matrix[curr[0]][curr[1]] == ".":
            ipt = 0
        else:
            ipt = 1
        calc(nums, ip, ipt, output)
        if len(output) < 2:
            return

        if output[0] == 0:
            matrix[curr[0]][curr[1]] = "."
        else:
            matrix[curr[0]][curr[1]] = "#"

        get_dir(curr, direction, output[1])

        if (curr[0], curr[1]) not in visited:
            visited.add((curr[0], curr[1]))
            count += 1
        print("COUNT = " + str(count))

    return count


def get_dir(curr, direction, ipt):
    if direction[0] == "UP":
        if ipt == 0:
            direction[0] = "LEFT"
            curr[1] -= 1
        else:
            direction[0] = "RIGHT"
            curr[1] += 1
    elif direction[0] == "DOWN":
        if ipt == 1:
            direction[0] = "LEFT"
            curr[1] -= 1
        else:
            direction[0] = "RIGHT"
            curr[1] += 1
    elif direction[0] == "LEFT":
        if ipt == 0:
            direction[0] = "DOWN"
            curr[0] += 1
        else:
            direction[0] = "UP"
            curr[0] -= 1
    else:
        if ipt == 0:
            direction[0] = "UP"
            curr[0] -= 1
        else:
            direction[0] = "DOWN"
            curr[0] += 1


if __name__ == "__main__":
    nums = []
    with open("./day11input") as f:
        for line in f:
            nums = [int(num) for num in line.split(",")]

    run(nums)

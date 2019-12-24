def calc(nums, base, ip, ipt, output, extension_map):
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

        run_tests(nums, ip, paramodes, opcode, base,
                  ipt, output, extension_map)
        if len(output) == 3:
            return


def expand_nums(nums, pos):
    for i in range(pos):
        nums.append(0)


def pos_exist(nums, pos, extension_map):
    if pos >= len(nums) and (pos not in extension_map):
        return False
    return True


def get_pos_val(nums, pos, extension_map):
    if pos_exist(nums, pos, extension_map):
        return nums[pos] if pos < len(nums) else extension_map[pos]
    else:
        return 0


def write_to_pos(nums, pos, extension_map, val):
    if pos < len(nums):
        nums[pos] = val
    else:
        extension_map[pos] = val


def run_tests(nums, ip, paramodes, opcode, base, ipt, output, extension_map):
    if opcode == 3 or opcode == 4 or opcode == 9:
        pos = nums[ip[0] + 1] \
                       if len(paramodes) < 1 or paramodes[0] == 0 \
                       else nums[ip[0] + 1] + base[0]
        if opcode == 9:
            if len(paramodes) < 1 or paramodes[0] != 1:
                base[0] += get_pos_val(nums, pos, extension_map)
            else:
                base[0] += nums[ip[0] + 1]
        elif opcode == 3:
            val = ipt()
            write_to_pos(nums, pos, extension_map, val)
        else:
            if len(paramodes) < 1 or paramodes[0] != 1:
                val = get_pos_val(nums, pos, extension_map)
            else:
                val = nums[ip[0] + 1]
            if val is not None:
                output.append(int(val))
        ip[0] += 2
    else:
        pos1 = nums[ip[0] + 1] if len(paramodes) < 1 or paramodes[0] == 0 \
            else nums[ip[0] + 1] + base[0]
        pos2 = nums[ip[0] + 2] if len(paramodes) < 2 or paramodes[1] == 0 \
            else nums[ip[0] + 2] + base[0]
        first_num, sec_num = 0, 0
        if len(paramodes) < 1 or paramodes[0] != 1:
            first_num = get_pos_val(nums, pos1, extension_map)
        else:
            first_num = nums[ip[0] + 1]
        if len(paramodes) < 2 or paramodes[1] != 1:
            sec_num = get_pos_val(nums, pos2, extension_map)
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
            if opcode < 3:
                if opcode == 1:
                    write_to_pos(nums, pos3, extension_map,
                                 first_num + sec_num)
                else:
                    write_to_pos(nums, pos3, extension_map,
                                 first_num * sec_num)
            else:
                if opcode == 7:
                    val = 1 if first_num < sec_num else 0
                    write_to_pos(nums, pos3, extension_map, val)
                else:
                    val = 1 if first_num == sec_num else 0
                    write_to_pos(nums, pos3, extension_map, val)
            ip[0] += 4


def run(nums):
    base = [0]
    ip = [2]

    matrix = [[0 for _ in range(30)] for _ in range(50)]
    extension_map = dict()
    ball_x = -1
    paddle_x = -1

    def ipt():
        if ball_x > paddle_x:
            return 1
        elif ball_x < paddle_x:
            return -1
        else:
            return 0

    while True:
        output = []
        calc(nums, base, ip, ipt, output, extension_map)
        if len(output) < 3:
            break
        x, y, tile_id = output[0], output[1], output[2]
        if x == -1 and y == 0:
            print("SCORE = " + str(tile_id))
            continue
        curr = matrix[x][y]

        if tile_id == 3:
            paddle_x = x
        if tile_id == 4:
            ball_x = x

        if curr == 0:
            matrix[x][y] = tile_id
        else:
            if curr == 2 and tile_id == 4:
                matrix[x][y] = 0


def pretty_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(str(matrix[i][j]), end="")
        print()


if __name__ == "__main__":
    nums = []
    with open("../input/day13input") as f:
        for line in f:
            nums = [int(num) for num in line.split(",")]
    run(nums)

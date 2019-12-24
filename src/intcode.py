class IntCode:
    def __init__(self, nums, base, ip, ipt):
        self.nums = nums
        self.base = base
        self.ip = ip
        self.ipt = ipt()
        self.extension_map = dict()

    def get_output(self):
        output = []
        while self.ip[0] < len(self.nums):
            num = str(self.nums[self.ip[0]])
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

            self.run_test(paramodes, opcode, output)
            if len(output) == 3:
                break
        return output

    def run_test(self, paramodes, opcode, output):
        if opcode == 3 or opcode == 4 or opcode == 9:
            pos = self.nums[self.ip[0] + 1] \
                        if len(paramodes) < 1 or paramodes[0] == 0 \
                        else self.nums[self.ip[0] + 1] + self.base[0]
            if opcode == 9:
                if len(paramodes) < 1 or paramodes[0] != 1:
                    self.base[0] += self._get_pos_val(pos)
                else:
                    self.base[0] += self.nums[self.ip[0] + 1]
            elif opcode == 3:
                self._write_to_pos(pos, self.ipt)
            else:
                if len(paramodes) < 1 or paramodes[0] != 1:
                    val = self._get_pos_val(pos)
                else:
                    val = self.nums[self.ip[0] + 1]
                if val is not None:
                    output.append(int(val))
            self.ip[0] += 2
        else:
            pos1 = self.nums[self.ip[0] + 1] \
                if len(paramodes) < 1 or paramodes[0] == 0 \
                else self.nums[self.ip[0] + 1] + self.base[0]
            pos2 = self.nums[self.ip[0] + 2] \
                if len(paramodes) < 2 or paramodes[1] == 0 \
                else self.nums[self.ip[0] + 2] + self.base[0]

            first_num, sec_num = 0, 0
            if len(paramodes) < 1 or paramodes[0] != 1:
                first_num = self._get_pos_val(pos1)
            else:
                first_num = self.nums[self.ip[0] + 1]

            if len(paramodes) < 2 or paramodes[1] != 1:
                sec_num = self._get_pos_val(pos2)
            else:
                sec_num = self.nums[self.ip[0] + 2]

            if 5 <= opcode < 7:
                if opcode == 5:
                    self.ip[0] = self.ip[0] + 3 if first_num == 0 else sec_num
                else:
                    self.ip[0] = self.ip[0] + 3 if first_num != 0 else sec_num
            else:
                pos3 = self.nums[self.ip[0] + 3] \
                       if len(paramodes) < 3 or paramodes[2] == 0 \
                       else self.nums[self.ip[0] + 3] + self.base[0]
                if opcode < 3:
                    if opcode == 1:
                        self._write_to_pos(pos3, first_num + sec_num)
                    else:
                        self._write_to_pos(pos3, first_num * sec_num)
                else:
                    if opcode == 7:
                        val = 1 if first_num < sec_num else 0
                        self._write_to_pos(pos3, val)
                    else:
                        val = 1 if first_num == sec_num else 0
                        self._write_to_pos(pos3, val)
                self.ip[0] += 4

    def _expand_nums(self, pos):
        for i in range(pos):
            self.nums.append(0)

    def _pos_exist(self, pos):
        if pos >= len(self.nums) and (pos not in self.extension_map):
            return False
        return True

    def _get_pos_val(self, pos):
        if self._pos_exist(pos):
            return self.nums[pos] \
                    if pos < len(self.nums) else self.extension_map[pos]
        else:
            return 0

    def _write_to_pos(self, pos, val):
        if pos < len(self.nums):
            self.nums[pos] = val
        else:
            self.extension_map[pos] = val

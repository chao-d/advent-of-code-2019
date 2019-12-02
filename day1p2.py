result = 0

nums = []
with open ("day1p1input") as f:
    for line in f:
        num = int(line.rstrip())
        nums.append(num)

def calc_fuel(num):
    if num <= 0:
        return 0
    else:
        curr = num // 3 - 2
        if curr <= 0:
            return 0
        else:
            return curr + calc_fuel(curr)

for num in nums:
    result += calc_fuel(num)

print(result)


result = 0

with open("../input/day1input") as f:
    for line in f:
        num = int(line.rstrip())
        result += num // 3 - 2

print(result)

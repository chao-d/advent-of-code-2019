def num_of_valid_passwords():
    res = 0
    for num in range(low, high + 1):
        if is_valid(num):
            res += 1
    return res


def is_valid(num):
    return is_nondec(str(num)) and has_double(str(num))


def is_nondec(num):
    for i in range(1, len(num)):
        if num[i] < num[i - 1]:
            return False
    return True


def has_double(num):
    i = 0
    while i < len(num) - 1:
        if num[i] == num[i + 1]:
            count = 0
            while i < len(num) - 1 and num[i] == num[i + 1]:
                i += 1
                count += 1
            if count == 1:
                return True
            if i == len(num) - 1:
                return False
        else:
            i += 1

    return False


if __name__ == "__main__":
    low, high = 359282, 820401
    print(num_of_valid_passwords())

def convert_to_list():
    with open("./day3input") as f:
        line = f.readline()
        firstline = [(step[0], int(step[1:])) for step in line.split(",")]
        line = f.readline()
        secondline = [(step[0], int(step[1:])) for step in line.split(",")]
        return firstline, secondline


def draw_line(line, x, y, is_second):
    currx, curry = x, y
    for d, num in line:
        if d == "U":
            currx, curry = mark_path(currx, curry, 0, -num, is_second)
        if d == "D":
            currx, curry = mark_path(currx, curry, 0, num, is_second)
        if d == "R":
            currx, curry = mark_path(currx, curry, num, 0, is_second)
        if d == "L":
            currx, curry = mark_path(currx, curry, -num, 0, is_second)


interx = []


def mark_path(currx, curry, delta_x, delta_y, is_second):
    if delta_x == 0:
        sign = delta_y // abs(delta_y)
        for i in range(1, abs(delta_y) + 1):
            if not is_second:
                grid[currx + sign * i][curry] = 1
            elif grid[currx + sign * i][curry] == 1 or \
                    grid[currx + sign * i][curry] == 3:
                grid[currx + sign * i][curry] = 3
            else:
                grid[currx + sign * i][curry] = 2

            if is_second and grid[currx + sign * i][curry] == 3:
                interx.append((currx + sign * i, curry))
        return currx + delta_y, curry
    elif delta_y == 0:
        sign = delta_x // abs(delta_x)
        for i in range(1, abs(delta_x) + 1):
            if not is_second:
                grid[currx][curry + sign * i] = 1
            elif grid[currx][curry + sign * i] == 1 and \
                    grid[currx][curry + sign * i] == 3:
                grid[currx][curry + sign * i] = 3
            else:
                grid[currx][curry + sign * i] = 2

            if is_second and grid[currx][curry + sign * i] == 3:
                interx.append((currx, curry + sign * i))
        return currx, curry + delta_x


def get_max(first, second):
    def _get_max(line):
        max_ver, max_hor = 0, 0
        min_ver, min_hor = 2 ** 31 - 1, 2 ** 31 - 1
        ver, hor = 0, 0
        for k, v in line:
            if k == "U":
                ver -= v
                min_ver = min(ver, min_ver)
            if k == "D":
                ver += v
                max_ver = max(ver, max_ver)
            if k == "L":
                hor -= v
                min_hor = min(hor, min_hor)
            if k == "R":
                hor += v
                max_hor = max(hor, max_hor)
        if min_ver == 2 ** 31 - 1:
            min_ver = 0
        if min_hor == 2 ** 31 - 1:
            min_hor = 0
        return (max(max_hor - min_hor, max(abs(min_hor), max_hor)),
                max(max_ver - min_ver, max(abs(min_ver), max_ver)))

    first_hor, first_ver = _get_max(first)
    sec_hor, sec_ver = _get_max(second)
    return max(first_ver, sec_ver), max(first_hor, sec_hor)


def min_dist(row, col):
    dist = 2 ** 31 - 1
    for x, y in interx:
        curr = abs(x - row) + abs(y - col)
        if curr < dist:
            dist = curr

    return dist


if __name__ == "__main__":
    first, second = convert_to_list()
    max_row, max_col = get_max(first, second)
    grid = [[0 for _ in range(2 * max_col + 2)] for _ in range(2 * max_row +
            2)]

    draw_line(first, max_row, max_col, False)
    draw_line(second, max_row, max_col, True)
    print(min_dist(max_row, max_col))

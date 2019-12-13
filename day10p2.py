import math
from functools import cmp_to_key


def get_all_asteroids(matrix):
    row_num, col_num = len(matrix), len(matrix[0])
    asteroids = []
    for i in range(row_num):
        for j in range(col_num):
            if matrix[i][j] == "#":
                asteroids.append((i, j))
    return asteroids


def best_location(matrix, asteroids):
    for ast in asteroids:
        mark_matrix(asteroids, ast, matrix)
    return get_largest(asteroids, matrix)


def mark_matrix(asteroids, ast, matrix):
    for a in asteroids:
        if a == ast:
            continue
        else:
            i, j = a[0], a[1]
            delta_x, delta_y = ast[0] - i, ast[1] - j
            if delta_x == 0:
                delta_y = int(abs(delta_y) / delta_y)
            elif delta_y == 0:
                delta_x = int(abs(delta_x) / delta_x)
            else:
                divs = math.gcd(delta_x, delta_y)
                delta_x = int(delta_x / divs)
                delta_y = int(delta_y / divs)
            has_other_ast = False
            i += delta_x
            j += delta_y
            while (i, j) != ast:
                if matrix[i][j] != ".":
                    has_other_ast = True
                    break
                i += delta_x
                j += delta_y
            if not has_other_ast:
                if matrix[a[0]][a[1]] == "#":
                    matrix[a[0]][a[1]] = 0
                matrix[a[0]][a[1]] += 1


def get_largest(asteroids, matrix):
    res = -1
    row, col = -1, -1
    for ast in asteroids:
        i, j = ast[0], ast[1]
        if res < matrix[i][j]:
            res = matrix[i][j]
            row, col = i, j
    return row, col


def get_slopes(origin, matrix, asteroids):
    slopes = dict()
    for ast in asteroids:
        x, y = ast[0], ast[1]
        if y == origin[1]:
            slope = -math.inf if x < origin[0] else math.inf
        elif x == origin[0]:
            slope = 0
        else:
            slope = (x - origin[0]) / (y - origin[1])
        slopes[ast] = slope
    return slopes


def sort_locations_by_slopes(slopes, origin):
    loc0, loc1 = [], []
    for k in slopes:
        if k[1] >= origin[1]:
            loc0.append(k)
        else:
            loc1.append(k)

    def custome_key0(p0, p1):
        if slopes[p0] > slopes[p1]:
            return -1
        elif slopes[p0] < slopes[p1]:
            return 1
        else:
            return dist_to_origin(p0) - dist_to_origin(p1)

    def custome_key1(p0, p1):
        if slopes[p0] > slopes[p1]:
            return 1
        elif slopes[p0] < slopes[p1]:
            return -1
        else:
            return dist_to_origin(p0) - dist_to_origin(p1)

    def dist_to_origin(p0):
        return pow((p0[0] - origin[0]), 2) + pow((p0[1] - origin[1]), 2)

    loc0 = sorted(loc0, key=cmp_to_key(custome_key0))
    loc1 = sorted(loc1, key=cmp_to_key(custome_key1))

    return clockwise_filter(loc0, loc1)


def clockwise_filter(loc0, loc1):
    res = []
    set0 = set(loc0)
    set1 = set(loc1)
    while set0 and set1:
        clockwise_helper(loc0, set0, res, slopes)
        clockwise_helper(loc1, set1, res, slopes)
    return res


def clockwise_helper(locs, loc_set, res, slopes):
    i = 0
    while i < len(locs):
        curr = locs[i]
        if curr not in loc_set:
            i += 1
        else:
            res.append(curr)
            loc_set.remove(curr)
            for j in range(i + 1, len(locs)):
                if slopes[locs[j]] != slopes[curr]:
                    break
            i = j


if __name__ == "__main__":
    matrix = []
    with open("./day10input") as f:
        for line in f:
            matrix.append([pos for pos in str(line).rstrip()])

    asteroids = get_all_asteroids(matrix)
    row, col = best_location(matrix, asteroids)
    origin = (row, col)
    asteroids.remove(origin)
    slopes = get_slopes(origin, matrix, asteroids)
    # print("slopes = " + str(slopes))
    locs = sort_locations_by_slopes(slopes, origin)

    for i, loc in enumerate(locs):
        print("pos = " + str(i + 1) + "  " + str(loc) + " " + str(slopes[loc]))

    x, y = locs[200][1], locs[200][0]
    print(x, y)
    print(100 * x + y)

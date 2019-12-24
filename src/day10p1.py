from math import gcd


def best_location(matrix):
    row_num, col_num = len(matrix), len(matrix[0])
    asteroids = []
    for i in range(row_num):
        for j in range(col_num):
            if matrix[i][j] == "#":
                asteroids.append((i, j))

    for ast in asteroids:
        mark_matrix(asteroids, ast, matrix)
    print(matrix)
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
                divs = gcd(delta_x, delta_y)
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
    print(res)
    return row, col


if __name__ == "__main__":
    matrix = []
    with open("../input/day10input") as f:
        for line in f:
            matrix.append([pos for pos in str(line).rstrip()])

    row, col = best_location(matrix)
    print(col, row)

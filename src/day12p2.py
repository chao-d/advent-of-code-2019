import re
import copy
from math import gcd


def run(pos, vel):
    num_of_steps = 0
    length = len(pos)
    dimensions = [set(), set(), set()]
    add_to_dimensions(pos, vel, dimensions)
    done_x, done_y, done_z = False, False, False
    steps_x, steps_y, steps_z = 0, 0, 0

    while True:
        mapping = {tuple(v): k for k, v in enumerate(pos)}
        sort_by_pos = []
        count_map = []
        for i in range(3):
            list0, map0 = [], dict()
            for j, p in enumerate(sorted(pos, key=lambda p: p[i])):
                list0.append(tuple(p))
                # map0[p[i]] = map0[p[i]] + 1 if p[i] in map0 else 1
                if p[i] not in map0:
                    map0[p[i]] = [j, j]
                else:
                    map0[p[i]][1] = j
            count_map.append(map0)
            sort_by_pos.append(list0)

        for i in range(3):
            for j in range(length):
                tmp = sort_by_pos[i][j]
                low, high = count_map[i][tmp[i]]
                vel[mapping[tmp]][i] += \
                    (length - high - 1) - (low)

        for i in range(length):
            for j in range(3):
                pos[i][j] += vel[i][j]

        num_of_steps += 1
        x, y, z = add_to_dimensions(pos, vel, dimensions)

        if x or y or z:
            if x and not done_x:
                print("x")
                done_x = True
                print(num_of_steps)
                steps_x = num_of_steps
            if y and not done_y:
                print("y")
                done_y = True
                print(num_of_steps)
                steps_y = num_of_steps
            if z and not done_z:
                print("z")
                done_z = True
                print(num_of_steps)
                steps_z = num_of_steps

        if done_x and done_y and done_z:
            return steps_x, steps_y, steps_z


def add_to_dimensions(pos, vel, dimensions):
    res = [False, False, False]
    for i in range(3):
        tmp = []
        for j in range(len(pos)):
            tmp.append(pos[j][i])
            tmp.append(vel[j][i])
        key = tuple(tmp)
        if key in dimensions[i]:
            res[i] = True
        else:
            dimensions[i].add(key)
    return tuple(res)


def lcm(steps):
    res = steps[0] * steps[1] // gcd(steps[0], steps[1])
    res = res * steps[2] // gcd(res, steps[2])
    return res


if __name__ == "__main__":
    pos = []
    with open("../input/day12input") as f:
        for line in f:
            line = re.split('=|, ', line.rstrip()[1:-1])
            pos.append([int(line[i]) for i in range(len(line)) if i % 2 == 1])

    vel = [[0 for _ in range(3)] for _ in range(len(pos))]

    origin_pos = copy.deepcopy(pos)
    origin_vel = copy.deepcopy(vel)

    steps = run(pos, vel)
    print(lcm(steps))

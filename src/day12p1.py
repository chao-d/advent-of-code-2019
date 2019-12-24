import re

STEPS = 1000


def run(pos, vel):
    for _ in range(STEPS):
        for i in range(len(pos)):
            for j in range(len(pos)):
                if i == j:
                    continue
                for k in range(3):
                    if pos[j][k] > pos[i][k]:
                        vel[i][k] += 1
                    elif pos[j][k] < pos[i][k]:
                        vel[i][k] -= 1

        for i in range(len(pos)):
            for j in range(3):
                pos[i][j] += vel[i][j]


def calc_energy(pos, vel):
    energy = 0
    for i in range(len(pos)):
        pot, kin = 0, 0
        for j in range(3):
            pot += abs(pos[i][j])
            kin += abs(vel[i][j])
        energy += pot * kin
    return energy


if __name__ == "__main__":
    pos = []
    with open("../input/day12input") as f:
        for line in f:
            line = re.split('=|, ', line.rstrip()[1:-1])
            pos.append([int(line[i]) for i in range(len(line)) if i % 2 == 1])

    vel = [[0 for _ in range(3)] for _ in range(len(pos))]

    run(pos, vel)
    print("pos = " + str(pos))
    print("vel = " + str(vel))

    energy = calc_energy(pos, vel)
    print("energy = " + str(energy))

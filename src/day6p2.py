def build_path(objs_map, src, target):
    path = []
    curr = src
    while curr != target:
        path.append(curr)
        curr = objs_map[curr]
    path.append(target)
    return path


def calc_length(p1, p2):
    i, j = -1, -1
    while p1[i] != "YOU" and p2[j] != "SAN":
        if p1[i] != p2[j]:
            break
        i -= 1
        j -= 1

    if p1[i] == "YOU" or p2[j] == "SAN":
        return len(p1) + len(p2) - 4

    return i - (-len(p1)) + j - (-len(p2))


if __name__ == "__main__":
    objs_map = dict()
    with open("../input/day6input") as f:
        for line in f:
            key_val = line.rstrip().split(")")
            objs_map[key_val[1]] = key_val[0]
    print(objs_map)
    path1 = build_path(objs_map, "YOU", "COM")
    print(path1)
    path2 = build_path(objs_map, "SAN", "COM")
    print(path2)
    print(calc_length(path1, path2))

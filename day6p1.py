from collections import deque


def topo_sort(objs_map):
    values = []
    queue = deque()
    curr = objs_map["COM"]
    queue.extend(curr)
    curr_val = 1
    while queue:
        size = len(queue)
        for _ in range(size):
            curr = queue.popleft()
            values.append((curr, curr_val))
            if curr in objs_map:
                queue.extend(objs_map[curr])
        curr_val += 1
    return values


def get_sum(values):
    sum = 0
    for _, v in values:
        sum += v
    return sum


if __name__ == "__main__":
    objs_map = dict()
    with open("./day6input") as f:
        for line in f:
            key_val = line.rstrip().split(")")
            if key_val[0] not in objs_map:
                objs_map[key_val[0]] = []
            objs_map[key_val[0]].append(key_val[1])
    values = topo_sort(objs_map)
    print(get_sum(values))

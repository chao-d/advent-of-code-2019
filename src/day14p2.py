from collections import OrderedDict


def calc_ore(mapping, outdegree, residue, val):
    vals = OrderedDict()
    vals["FUEL"] = val
    nums = []
    while vals:
        curr = vals.popitem(False)
        if outdegree[curr[0]] > 0:
            vals[curr[0]] = curr[1]
            continue
        total = curr[1]
        if curr[0] in residue:
            if residue[curr[0]] >= mapping[curr[0]]["val"]:
                need = mapping[curr[0]]["val"] * \
                    (residue[curr[0]] // mapping[curr[0]]["val"])
                total -= need
                residue[curr[0]] -= need
        else:
            residue[curr[0]] = 0
        ratio = 1
        if total > mapping[curr[0]]["val"]:
            ratio = -(total // -mapping[curr[0]]["val"])
            if ratio != total // mapping[curr[0]]["val"]:
                residue[curr[0]] += ratio * mapping[curr[0]]["val"] - total
        for k, v in mapping[curr[0]].items():
            if k == "val":
                continue
            if k == "ORE":
                nums.append(v * ratio)
                continue
            outdegree[k] -= 1
            if k not in vals:
                vals[k] = 0
            vals[k] += v * ratio
    return sum(nums)


if __name__ == "__main__":
    mapping = dict()
    outdegree = dict()
    with open("../input/day14input") as f:
        for line in f:
            sep = line.rstrip().split(" => ")
            right = sep[1].split(" ")
            mapping[right[1]] = {"val": int(right[0])}
            if right[1] != "ORE" and right[1] not in outdegree:
                outdegree[right[1]] = 0
            left = [ele.split(" ") for ele in sep[0].split(", ")]
            for pair in left:
                mapping[right[1]][pair[1]] = int(pair[0])
                if pair[1] == "ORE":
                    continue
                if pair[1] not in outdegree:
                    outdegree[pair[1]] = 0
                outdegree[pair[1]] += 1

    ore = int(1e12)
    low, high = 0, int(1e12)
    while low + 1 < high:
        residue = dict()
        mid = (low + high) // 2
        if calc_ore(mapping, outdegree, residue, mid) <= ore:
            low = mid
        else:
            high = mid - 1

    if calc_ore(mapping, outdegree, residue, high) <= ore:
        print("value = ", high)
    else:
        print("value = ", low)

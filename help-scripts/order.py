from functools import reduce
import random

# Two groups of size 10
# Rest will be whatever left remains
GROUP_SIZES = [10, 10]


def to_groups(seq, group_sizes):
    groups = {}
    seq_index = 1
    group_index = 1

    total_sizes = reduce(lambda x, y: x + y, group_sizes)

    if total_sizes < len(seq):
        group_sizes.append(len(seq) - total_sizes)

    for size in group_sizes:
        elements_taken = 0
        group_name = "Group {}".format(group_index)
        groups[group_name] = []
        while elements_taken < size and seq_index < len(seq):
            groups[group_name].append(seq[seq_index])
            seq_index += 1
            elements_taken += 1
        group_index += 1

    return groups


def print_stats(teams):
    teams_count = len(teams)
    total_minutes = teams_count * 6
    total_hours = total_minutes / 60

    print("Total number of teams: {}".format(teams_count))
    print("Total minutes of presenting: {}".format(total_minutes))
    print("Total hours of presenting: {}".format(total_hours))


teams = open("teams").read().split("\n")

teams = [team.strip() for team in teams if team.strip() != ""]
random.shuffle(teams)

groups = to_groups(teams, GROUP_SIZES)

print_stats(teams)

result = []

for key in groups:
    result.append("## " + key)
    result.append("\n".join(list(map(lambda x: "* " + x, groups[key]))))

handler = open("schedule.md", "w")
handler.write("\n".join(result))
handler.close()

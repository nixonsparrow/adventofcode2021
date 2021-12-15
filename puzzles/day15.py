from .methods import txt_opener


def enlarge_grid(graph):
    new_graph = []

    # enlarge existing rows
    for row in graph:
        new_row = []
        for i in range(5):
            for nr in row:
                nr_i = int(nr) + i
                new_row.append(nr_i if nr_i < 10 else nr_i - 9)
        new_graph.append(''.join(list(map(str, new_row))))

    # add new rows
    for i in range(len(graph), len(graph) * 5):
        new_row = []
        for nr in new_graph[i - len(graph)]:
            new_row.append(int(nr) + 1 if int(nr) + 1 < 10 else 1)
        new_graph.append(''.join(list(map(str, new_row))))

    return new_graph


def adjacent(slot, graph):
    for a, b in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
        if len(graph) > slot[0] + a >= 0 and len(graph[0]) > slot[1] + b >= 0:
            yield slot[0] + a, slot[1] + b


def get_lowest_risk(graph):
    visited = [(0, 0)]
    risk_dict = {0: [(0, 0)]}

    for risk in range(len(graph) * len(graph)):
        if risk not in risk_dict.keys(): risk_dict[risk] = []
        current_slots = risk_dict[risk]
        for current_slot in current_slots:
            for slot in adjacent(current_slot, graph):
                if slot == (len(graph) - 1, len(graph) - 1):
                    return risk + int(graph[len(graph) - 1][len(graph) - 1])

                if slot not in visited:
                    new_risk = int(graph[slot[0]][slot[1]]) + risk
                    if new_risk in risk_dict.keys():
                        risk_dict[new_risk].append(slot)
                    else:
                        risk_dict[new_risk] = [slot]
                    visited.append(slot)


def part1(input_file):
    final_input = txt_opener(input_file, '\n', force_str=True)
    return get_lowest_risk(final_input)


def part2(input_file):
    final_input = txt_opener(input_file, '\n', force_str=True)
    enlarged_grid = enlarge_grid(final_input)
    return get_lowest_risk(enlarged_grid)

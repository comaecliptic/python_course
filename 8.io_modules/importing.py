import graph_components as gc


graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 5],
    4: [2],
    5: [2, 3],
    6: [],
}
print(gc.count_components(graph))

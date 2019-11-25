def dfs(graph, vertex, visited):
    """Walk through all graph vertices,
    visiting each vertex only once.

    Parameters
    ----------
    graph : dict of {int: list of int}
        Graph in form of adjacency list.
    vertex : int
        Start vertex.
    visited: dict of {int: bool}
        Tracker of visited vertices.
    """
    visited[vertex] = True
    for adjacent in graph[vertex]:
        if not visited[adjacent]:
            dfs(graph, adjacent, visited)


def count_components(graph):
    """Return number of connected components of
    an input graph.

    Parameters
    ----------
    graph : dict of list of int
        Graph in form of adjacency list.

    Returns
    -------
    result : int
        Number of components.
    """
    visited = {vertex: False for vertex in graph}
    vertex_list = [vertex for vertex in graph]
    result = 0
    while vertex_list:
        dfs(graph, vertex_list[0], visited)
        for vertex, status in visited.items():
            if vertex in vertex_list and status:
                vertex_list.remove(vertex)
        result += 1
    return result


graph1 = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1, 4],
    4: [1, 3, 5],
    5: [4],
}
graph2 = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1, 4],
    4: [1, 3, 5],
    5: [4],
    6: [7, 8],
    7: [6, 8],
    8: [6, 7],
    9: [10],
    10: [9],
}
assert count_components(graph1) == 1
assert count_components(graph2) == 3

# for first task
print('Да, исполняется.')



def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)
    distance = [float("inf")] * len(graph.data)
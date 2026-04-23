class Graph:
    def __init__(self, num_nodes, edges, directed = False, weighted = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                # include weight
        

def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)
    distance = [float("inf")] * len(graph.data)
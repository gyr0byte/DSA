class Graph:
    def __init__(self, num_nodes, edges, directed = False, weighted = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_edges)]
        self.weight = [[] for _ in range(num_edges)]
        for edge in edges:
            if self.weighted:
                # include weights
                node1, node2, weight = edge
                
            else:
                # work without weights

num_node5 = 9
edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

num_node6 = 5
edges6 = [(0,1), (1,2), (2,3), (2,4), (4,2), (3,0)]

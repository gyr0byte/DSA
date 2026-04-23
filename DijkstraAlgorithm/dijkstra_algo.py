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
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                # work without weights
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)
    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += f"{i}: {list(zip(nodes, weights))}"
        else:
            for i, nodes in enumerate(self.data):
                result += f"{i}: {nodes}\n"
        return result
        

def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)
    distance = [float("inf")] * len(graph.data)
    queue = []

    distance[source] = 0
    queue.append(source)
    idx = 0
    
    while idx < len(queue) and not visited[target]:
        current =  queue[idx]
        idx += 1

        #update the distance of all the neighbors
        update_distances(graph, current, distance, )
        
        # find the first unvisited node with the smallest distance
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)
        
        visited[current] = True
    
    return distance[target]
        
def update_distances(graph, current, distance, parent = None):
    """ Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current

def pick_next_node(distance, visited):
    """Pick the next unvisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]

    return min_node
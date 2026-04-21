class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return "\n".join([f"{n}: {neighbors}"for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph)
    
    discovered[root] = True
    queue.append(root)
    idx = 0
    
    while idx < len(queue):
        # dequeue
        current = queue[idx]
        idx += 1
        
        # check all edges of current
        for node in self.data[current]:
            if not discovered[node]:
                discovered[node] = True
                queue.append(node)

    return queue


def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph)
    
    discovered[root] = True
    queue.append(root)
    idx = 0
    
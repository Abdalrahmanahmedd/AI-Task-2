from queue import Queue

def bfs_with_path(graph, start):
    q = Queue()
    q.put(start)
    visited = {node: False for node in graph}
    parent = {node: None for node in graph}  # to track the path
    visited[start] = True

    while not q.empty():
        node = q.get()
        print(f"Visited: {node}")

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                q.put(neighbor)

    # print the path for each node
    print("\nPaths from the start node:")
    for node in graph:
        if visited[node]:
            path = []
            current = node
            while current is not None:
                path.insert(0, current)
                current = parent[current]
            print(f"Path to {node}: {path}")

# Example graph
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

bfs_with_path(graph, 0)

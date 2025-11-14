def dfs_with_path(graph, start):
    visited = {node: False for node in graph}
    parent = {node: None for node in graph}  # to keep track of the path
    stack = [start]
    visited[start] = True

    while stack:
        current = stack.pop()
        print(f"Visited: {current}")

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                stack.append(neighbor)

    # print the path for each node
    print("\nPaths from the start node:")
    for node in graph:
        if visited[node]:
            path = []
            curr = node
            while curr is not None:
                path.insert(0, curr)
                curr = parent[curr]
            print(f"Path to {node}: {path}")


# Example graph
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

dfs_with_path(graph, 0)

def topological_sort(graph):
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    visited = set()
    stack = []

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Reverse the stack for topological order

# Example usage:
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}
print(topological_sort(graph))  # Output: ['B', 'A', 'D', 'C', 'E', 'H', 'F', 'G']

#01/2025, Quenten welch
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    traversal = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            traversal.extend(dfs(graph, neighbor, visited))
    return traversal

# Example Usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(dfs(graph, 'A'))  # Output: ['A', 'B', 'D', 'E', 'F', 'C']

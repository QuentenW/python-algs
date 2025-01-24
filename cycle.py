#01/2025, Quenten welch
def has_cycle(graph, node, visited, parent):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, node):
                return True
        elif parent != neighbor:
            return True
    return False

def detect_cycle(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            if has_cycle(graph, node, visited, None):
                return True
    return False

# Example Usage:
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}
print(detect_cycle(graph))  # Output: True

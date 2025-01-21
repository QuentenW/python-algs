def has_cycle(graph, node, visited, parent):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True
    return False

def is_cyclic(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            if has_cycle(graph, node, visited, None):
                return True
    return False

# Example usage:
graph = {
    0: [1, 2],
    1: [

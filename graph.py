from collections import defaultdict, deque
#01/2025, Quenten welch

# [['a', 'b'], ['b', 'c'], ['b', 'd'], ['b', 'c'], ['c', 'd']]
def find_installation_order(dependencies):
    # Create a graph and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Build the graph and compute in-degrees
    for a, b in dependencies:
        #add key value pair or add b to dependency list if exists
        graph[a].append(b)
        print(a, graph[a])
        #b is dependant on a, track this dependency
        in_degree[b] += 1
        if a not in in_degree:
            in_degree[a] = 0
  
    
    # Initialize the queue with nodes that have zero in-degree
    queue = deque()
    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)
    
    # List to store the installation order
    install_order = []
    
    while queue:
        current = queue.popleft()
        install_order.append(current)
        
        # Decrease in-degree for all neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if there's a cycle (not all nodes are processed)
    if len(install_order) != len(in_degree):
        return "Cycle detected"
    
    return install_order

# Example usage
dependencies = [['a', 'b'], ['b', 'c'], ['b', 'd'], ['b', 'c'], ['c', 'd']]
order = find_installation_order(dependencies)
# print(order)  # Expected Output: ['a', 'b', 'c', 'd']
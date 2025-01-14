#construct directed graph
#get in_degree of each node
#search in_degree, if in_degree[x] is 0 then add to queue
#while queue.length != 0
### pop program from q and set to current,
### for each item in graph[current] decrement in_degree (we have addressed the dependency)
### if in_degree[item] is 0 add to queue

for a, b in input:
    graph[a].append(b)
    in_degree[b] += 1
    if a not in in_degree:
        in_degree[a] == 0

for node in in_degree:
    if node == 0:
        que.append(node)

while que:
    current = que.popleft
    for neighbor in graph[current]:
        in_degree[neighbor] -=1
        if in_degree[neighbor] == 0:
            que.append(neighbor)
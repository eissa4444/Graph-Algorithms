def dfs_iterative(graph,vertex):
	stack,visited = [vertex],set()
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited

#Testing the algorithims
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
print(dfs_iterative(graph,'A'))
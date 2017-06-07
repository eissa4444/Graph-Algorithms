def bfs(graph,vertex):
	queue,visited = [vertex],set()
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
	return visited

#######3Testing the algorithims########
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
		 
print("breadth first search: "+str(bfs(graph,'A')))

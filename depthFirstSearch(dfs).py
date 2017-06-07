def dfs_iterative(graph,vertex):
	stack,visited = [vertex],set()
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited

def dfs_recursive(graph,vertex,visited=None):
	if visited == None:
		visited = set()
	visited.add(vertex)
	for next in graph[vertex] - visited:
		dfs_recursive(graph,next,visited)
	return visited
	
#get all possible paths from start vertex to a target vertex
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

#######3Testing the algorithims########
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print("dfs-iterative: "+str(dfs_iterative(graph,'A')))
print("dfs-recursive: "+str(dfs_recursive(graph,'A')))
print("all possible paths from vertx A to F is: " + str(list(dfs_paths(graph,'A','F'))))

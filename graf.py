# Breadth-first search (BFS) with a graph

graf = [[0, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [],
        [1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]



def bfs(graph, queque, visited, road):
    if len(visited) == len(graph):
        return road
    else:
        first = queque[0]
        pivot = 0
        for i in graph[first]:
            if i == 1:
                queque.append(pivot)
            pivot += 1
        road.append(first)
        queque.pop(0)
        visited.add(first)
        return bfs(graph, queque, visited, road)

                
que = [0]
v = set()
result = []


w = bfs(graf, que, v, result)
print(w)

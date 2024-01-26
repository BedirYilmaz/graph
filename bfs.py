import queue

# depth first search

graph = {
    "A": ["B","C","D"],
    "B": ["E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"],
    "G": [],
    "H": [],
    "I": [],
    "J": []
}

    
def bfs (edge):
    print(edge)
    for i in range(len(graph[edge])):
        que.put(graph[edge][i])
    bfs(que.get())
    
print("******* breadth first search ******* \n")
que = queue.SimpleQueue()
bfs("A")





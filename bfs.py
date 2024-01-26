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
    if not que.empty():
        bfs(que.get())

def bfs_iterative (edge):
    que.put(edge)

    discovered = []
    while not que.empty():
        node = que.get()
        if node not in discovered:
            for neighbor in graph[node]:
                que.put(neighbor)
            discovered.append(node)
            print(node)


print("******* breadth first search   ******* \n")
print("\n*******       recursive      ******* \n")
que = queue.SimpleQueue()
bfs("A")
print("\n*******       iterative      ******* \n")
que = queue.SimpleQueue()
bfs_iterative("A")




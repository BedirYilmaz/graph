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

def dfs (edge):
    print(edge)

    for next_edge in graph[edge]:
        dfs(next_edge)
    
    
print("******* depth first search   ******* \n")
dfs("A")





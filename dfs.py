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
    
def dfs_iterative (root):
    mem = []
    discovered = []
    mem.append(root)

    while len(mem) > 0:
        node = mem.pop()
        print(node)
        if node not in discovered:
            for neighbor in graph[node]:
                mem.append(neighbor)
            discovered.append(node)
     
print("******* depth first search   ******* \n")
print("\n*******       recursive      ******* \n")
dfs("A")
print("\n*******       iterative      ******* \n")
dfs_iterative("A")





import bfs

# Initialise G using the graph from earlier
example_vertices = [1, 2, 3, 4, 5] 
example_adj_list = { 
    1: [2, 3], 
    2: [2, 4], # Includes the self-loop 
    3: [4], 
    4: [3, 5], # 3 and 4 share a bidirectional edge 
    5: [] # Sink node 
} 
G = bfs.Graph(example_vertices, example_adj_list) 

# Run the search starting from vertex 1 
distances, predecessors = bfs.breadth_first_search(G, 1)

print("Shortest Distances from Source (1):")
print(distances) 

print("\nPredecessor (Parent) Nodes:")
print(predecessors)

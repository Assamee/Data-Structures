# import the Double-Ended Queue (for a real implementation)
from collections import deque

# Define the basic Graph class
class Graph: 
	def __init__(self, vertices, adjacency_list): 
		self.vertices = vertices # List of vertices
		self.adjacency_list = adjacency_list # Dictionary

# Let G be the Graph, and s be the source node
def breadth_first_search(G, s):

    # Step 1: Set up with Empty Dictionaries
    colour = {}
    d = {}
    pi = {}
    
    # Initialise all vertices to White, distance infinity, predecessor None
    for v in G.vertices:
        colour[v] = "WHITE"
        d[v] = float('inf')
        pi[v] = None
        
    # Source Vertex: Set s to Grey, distance to 0
    colour[s] = "GREY"
    d[s] = 0
    pi[s] = None
    
    # Setup Queue: We use a deque (double-ended queue) instead of a standard Python list
    # because removing from the front of a list is O(n), whereas deque.popleft() is O(1)
    Q = deque()
    Q.append(s)
    
    # Discovery Loop: While Q isn't empty, dequeue the head vertex u
    while len(Q) > 0:
        u = Q.popleft()
        
        # Current Neighbours: For each neighbour v of u
        for v in G.adjacency_list[u]:
            # If v is White (newly discovered), update and enqueue
            if colour[v] == "WHITE":
                colour[v] = "GREY"
                d[v] = d[u] + 1
                pi[v] = u   # Set u to be its predecessor
                Q.append(v)
                
        # Completion: Colour u Black (finished)
        colour[u] = "BLACK"
        
    return d, pi


if __name__ == "__main__":
# Initialise G using the graph from earlier
	example_vertices = [1, 2, 3, 4, 5] 
	example_adj_list = { 
		1: [2, 3], 
		2: [2, 4], # Includes the self-loop 
		3: [4], 
		4: [3, 5], # 3 and 4 share a bidirectional edge 
		5: [] # Sink node 
	} 
	G = Graph(example_vertices, example_adj_list) 
	
	# Run the search starting from vertex 1 
	distances, predecessors = breadth_first_search(G, 1)
	
	print("Shortest Distances from Source (1):")
	print(distances) 
	
	print("\nPredecessor (Parent) Nodes:")
	print(predecessors)

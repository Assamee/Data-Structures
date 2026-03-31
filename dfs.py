# Define the basic Graph class
class Graph:
    def __init__(self, vertices, adjacency_list):
        self.vertices = vertices # List of Vertices
        self.adjacency_list = adjacency_list # Dictionary

# Let G be the Graph
def depth_first_search(G):
    
    # Set up with empty dictionaries
    colour = {}
    d = {}      # Discovery Times
    f = {}      # Finish Times
    pi = {}     # Predecessors
    
	# Initialise all vertices to White and predecessors to None
    for v in G.vertices:
        colour[v] = "WHITE"
        pi[v] = None
        
    # Set the global time counter to 0. 
    # We use the 'nonlocal' keyword inside the nested function to access the variable globally
    time = 0  
    
    # --- Recursive Explorer Function (runs for each vertex u) ---
    def dfs_visit(u):
        
        # nonlocal keyword so python treats time as a global variable
        nonlocal time
        
        # Discovery: Increment the time counter
        time += 1            
        
        # Update Vertex (u) Info
        d[u] = time          
        colour[u] = "GREY"      
        
        # Explore the paths of each neighbour of u
        for v in G.adjacency_list[u]:
            if colour[v] == "WHITE":
                pi[v] = u       # Set parent to be u
                dfs_visit(v)    # Recursive call to go deeper into the path
                
        # Increment Time once each neighbour's path has been explored
        time += 1            
        
        # Final Vertex Update for u
        f[u] = time          # Set u's finish time
        colour[u] = "BLACK"  # Colour u Black
    
    # Forest Loop: Iterate through every vertex u in the graph
    for u in G.vertices:
        # If u is White, call the recursive exploration function DFS_Visit(u)
        if colour[u] == "WHITE":
            dfs_visit(u)
            
    return d, f, pi

# ---------------------------------------------------------
# Works with the code above (copy-paste into VS code)
# ---------------------------------------------------------
if __name__ == "__main__":
    
    # Initialise G using the same graph for the BFS example
    example_vertices = [1, 2, 3, 4, 5]
    example_adj_list = {
        1: [2, 3],
        2: [2, 4],  # Includes the self-loop
        3: [4],
        4: [3, 5],  # 3 and 4 share a bidirectional edge
        5: []       # Sink node
    }
    
    G = Graph(example_vertices, example_adj_list)
    
    # Run the search
    discovery, finish, predecessors = depth_first_search(G)
    
    print("Discovery Times (d):")
    print(discovery)
    
    print("\nFinish Times (f):")
    print(finish)
    
    print("\nPredecessor (Parent) Nodes:")
    print(predecessors)
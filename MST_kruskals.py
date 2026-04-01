class Graph:
    def __init__(self, vertices, edges):
        # The list of all vertices in the graph
        self.vertices = vertices
        # The list of edges, where each edge is a tuple in the format: (weight, u, v)
        self.edges = edges

# The Hash Map (dictionary) used to map a vertex to its Representative
# Declared globally so our isolated functions can access it without passing it as a parameter
rep = {}

# Creates a one element set x
def makeset(x):
    rep[x] = x

# Returns the representative of the subset containing x
def find(x):
    # Base Case: If x is its own representative, we have found the root of the tree. Stop and return it.
    if rep[x] == x:
        return x
        
    # Recursive Step: If x is not the root, dig deeper and update x's representative (and all of its parents' reps) to be the root
    rep[x] = find(rep[x])
    return rep[x]

def union(x, y):
    # Constructs the union of the disjoint subsets containing x and y
    root_x = find(x)
    root_y = find(y)

    # Arbitrarily make root_x the representative for both sets (making the newly combined set)
    if root_x != root_y:
        rep[root_y] = root_x

def kruskal_mst(G):
    # Clear the global dictionary in case we run the algorithm multiple times
    rep.clear()
    
    # The list of chosen edges that form the Minimum Spanning Tree
    mst = []

    # Setup: Start with a Forest where every vertex is its own isolated tree
    for v in G.vertices:
        makeset(v)
    # Now rep = {"A":"A", "B":"B" ...}

    # Sort Edges: List all the edges in ascending order of their weight
    # sorted() Works without extra parameters because the weights are the first elements in each edge's tuple
    sorted_edges = sorted(G.edges) 

    # Greedy Loop: Iterate through the sorted edges
    for edge in sorted_edges:
        weight, u, v = edge
        
        # If the vertices have different representatives (to avoid cycles):
        if find(u) != find(v):
            # Add the edge to the MST
            mst.append(edge)
            # Merge the two trees into one
            union(u, v)
            
            # Pruning Step: Stop early if we have the required V - 1 edges
            if len(mst) == len(G.vertices) - 1:
                break

    return mst

if __name__ == "__main__":
    # A dummy list of 6 vertices
    vertices = [1, 2, 3, 4, 5, 6]
    
    # A dummy list of edges in the format (weight, u, v)
    edges = [
        (1, 1, 4), (2, 5, 2), (3, 4, 5), (4, 3, 6),
        (5, 1, 2), (6, 3, 4)
    ]
    
    # Instantiate the Graph and run Kruskal's algorithm
    G = Graph(vertices, edges)
    mst_result = kruskal_mst(G)
    
    print("Edges in the Minimum Spanning Tree:")
    for weight, u, v in mst_result:
        print(f"Edge ({u}, {v}) with weight {weight}")

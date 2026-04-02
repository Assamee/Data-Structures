import heapq # Import to use a heap queue (a Priority Queue)

class Graph:
    def __init__(self, vertices, adj_list):
        # The list of all vertices in the graph
        self.vertices = vertices
        # The adjacency list format: {node: [(weight, neighbour), ...]}
        self.adj = adj_list

def prim_mst(G, start_node):
    # The list of edges (tuples) that will make up the final MST
    mst_edges = []
    
    # The set of vertices we have already reached and connected (Set U)
    visited_set = {start_node}
    
    # A Min-Heap data sructure storing the "Frontier" of available edges
    # Edges are tuples in the format: (weight, u, v)
    frontier_edges = []

    # G.adj[start_node] is the list of adjacent edges
    # Add these edges to the Priority Queue (Min-Heap)
    for weight, v in G.adj[start_node]:
        heapq.heappush(frontier_edges, (weight, start_node, v))

    # The Greedy Loop that runs until we have V-1 edges
    # If frontier_edges is empty, then there are no edges to reach leftover unvisited nodes (prevents an error for disconnected graphs)
    while frontier_edges and len(mst_edges) < len(G.vertices) - 1:
        
        # 3. The Light Edge: Pop the absolute cheapest edge from the heap
        weight, u, v = heapq.heappop(frontier_edges)

        # 4. Update: If the destination v is NOT in the visited set (it is unvisited)
        if v not in visited_set:
            # Move vertex v into the visited set U
            visited_set.add(v)
            # Add the chosen edge to our MST
            mst_edges.append((u, v, weight))

            # Identify the new Cut: Add all edges from the newly visited vertex v
            for next_weight, neighbour in G.adj[v]:
                if neighbour not in visited_set:
                    heapq.heappush(frontier_edges, (next_weight, v, neighbour))

    return mst_edges

if __name__ == "__main__":
    # Example Graph 
    nodes = ['A', 'B', 'C', 'D']
    
    # Adjacency list format: {node: [(weight, neighbour), ...]}
    adj = {
        'A': [(10, 'C'), (5, 'B')],
        'B': [(5, 'A'), (2, 'C'), (5, 'D')],
        'C': [(10, 'A'), (2, 'B'), (1, 'D')],
        'D': [(5, 'B'), (1, 'C')]
    }

    my_graph = Graph(nodes, adj)
    mst = prim_mst(my_graph, 'A')

    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} --({weight})-- {v}")
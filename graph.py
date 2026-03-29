# Simple Graph Data Structure Implementation in Python
class graph:
    # Constructor method
    def __init__(self, edges, vertices):
        # Tuple means that there can be directed graphs
        self.edges = set(edges)  # P3 = {(node1 -> node2), (node2 -> node3)}
        self.vertices = set(vertices) # P3 = {node1, node2, node3}
    
    # Get an edge
    def getEdges(self):
        return self.edges
    
    # Get a Node
    def getNodes(self):
        return self.vertices
    
    # size is defined as the number of edges in the graph
    def getSize(self):
        size = 0
        calculatedEdges = set()
        for i in self.edges:
            if i not in calculatedEdges and i[::-1] not in calculatedEdges:
                calculatedEdges.add(i)
                size += 1
        return size

    
    def getNeighbours(self, vertex):
        if vertex not in self.vertices:
            return "Vertex not Found. "
        neighbours = []
        for v in self.vertices:
            if (v, vertex) in self.edges or (vertex, v) in self.edges:
                neighbours.append(v)
        return neighbours
    
        # return [vertex for v in self.vertices if ((v, vertex) in self.edges) or ((vertex, v) in self.edges)]

    # Returns a list of edges (tuples) that contain the given vertex
    def getIncidentEdges(self, vertex):
        # [] to create and return a new list
        # for each edge in the set of edges, add an edge to the list, if the given vertex is in that edge
        return [edge for edge in self.edges if vertex in edge]

    # Add a node to the Graph
    def addNode(self, value):
        self.vertices.add(value)

    # Add an edge to the Graph
    def addEdge(self, node1, node2):
        self.vertices.add(node1)
        self.vertices.add(node2)
        self.edges.add((node1, node2))

    # Checks if a node exists in the graph
    def contains(self, node):
        if node in self.vertices:
            return True
        else:
            return False
        
    # Remove a node from the Graph
    def removeNode(self, node):
        if not self.contains(node):
            return 'Vertex not Found. '
        
        
        incidentEdges = self.getIncidentEdges(node)
        self.vertices.remove(node)

        if incidentEdges:
            for i in incidentEdges:
                self.edges.remove(i)

    # Remove an edge from the Graph
    def removeEdge(self, node1, node2):
        edge = (node1, node2)
        if edge in self.edges:
            self.edges.remove(edge)



p3edges = {("node1", "node2"), ("node2", "node1"), ("node2", "node3"), ("node3", "node2"), }
p3vertices = {"node1", "node2", "node3"}
p3 = graph(p3edges, p3vertices)
#print(p3.getEdges())
#print(p3.getNodes())

p3.addNode("node4")
p3.addNode("node5")
p3.addEdge("node4", "node5")
p3.addEdge("node5", "node4")
p3.addEdge("node3", "node4")
p3.addEdge("node4", "node3")

print("\n =========== AFTER ===========\n")
#print(p3.getEdges())
#print(p3.getNodes())

print(p3.contains("node5"))

p3.removeNode("node5")

print(p3.contains("node5"))

print(p3.getEdges())
print(p3.getNodes())

#p3.removeEdge("node2", "node1")
#p3.removeEdge("node3", "node2")
#p3.removeEdge("node4", "node3")

print(p3.getEdges())
print(p3.getNodes())

print(p3.getSize())
class DirectedGraph:
    def __init__(self):
        # Dictionary to store the graph: node -> list of neighbors
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, u, v):
        # Add nodes if they don't exist
        self.add_node(u)
        self.add_node(v)
        # Add directed edge u -> v
        self.adj_list[u].append(v)

    def display(self):
        for node, neighbors in self.adj_list.items():
            print(f"{node} -> {neighbors}")

# Example Usage
if __name__ == "__main__":
    g = DirectedGraph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('D', 'A') # Creates a cycle
    
    print("Adjacency List:")
    g.display()
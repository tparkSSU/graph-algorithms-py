from node import Node
from simple_heap import MinHeap

class DirectedGraph:
    def __init__(self):
        # Dictionary to store the graph: Node -> list of (Node, weight)
        self.adj_list = {}
        # Helper to map string names to Node objects
        self.name_to_node = {}

    def get_node(self, node_name):
        if node_name not in self.name_to_node:
            new_node = Node(node_name)
            self.name_to_node[node_name] = new_node
            self.adj_list[new_node] = []
        return self.name_to_node[node_name]

    def add_node(self, node_name):
        self.get_node(node_name)

    def add_edge(self, u_name, v_name, d):
        # Add nodes if they don't exist and get Node objects
        u_node = self.get_node(u_name)
        v_node = self.get_node(v_name)
        
        # Add directed edge u -> v with weight d
        self.adj_list[u_node].append((v_node, d))

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                     u = parts[0].strip()
                     v = parts[1].strip()
                     d = float(parts[2].strip())
                     self.add_edge(u, v, d)

    def dijkstra(self, start_node_name):
        # Reset all nodes
        for node in self.adj_list:
            node.distance = float('inf')
            node.visited = False
            node.parent = None
        
        start_node = self.get_node(start_node_name)
        start_node.distance = 0
        
        heap = MinHeap()
        heap.insert(start_node)
        
        while heap.heap:
            u = heap.extract_min()
            
            if u is None: # heap empty logic
                break

            if u.visited:
                continue
            u.visited = True
            
            if u.distance == float('inf'):
                break

            for v, weight in self.adj_list[u]:
                if not v.visited:
                    new_dist = u.distance + weight
                    if new_dist < v.distance:
                        v.distance = new_dist
                        v.parent = u
                        heap.insert(v)

    def get_shortest_path(self, target_node_name):
        target = self.get_node(target_node_name)
        if target.distance == float('inf'):
            return [], float('inf')
        
        path = []
        curr = target
        while curr:
            path.append(curr.name)
            curr = curr.parent
        return path[::-1], target.distance # Return reversed path (start to end)

    def get_graph_data(self):
        nodes = []
        edges = []
        for node_name in self.name_to_node:
            nodes.append({"data": {"id": node_name}})
        
        for u_node, neighbors in self.adj_list.items():
            for v_node, weight in neighbors:
                edges.append({
                    "data": {
                        "source": u_node.name,
                        "target": v_node.name,
                        "weight": weight
                    }
                })
        return {"nodes": nodes, "edges": edges}

    def print_path(self, target_node_name):
        path, cost = self.get_shortest_path(target_node_name)
        if not path:
             print(f"No path to {target_node_name}")
             return

        # Format for printing: A(0) -> B(10) ... needs distance reconstruction if we want (curr.distance) style
        # Simplified for now just matching previous output style roughly or just printing list
        # Actually let's keep previous print logic but use the helper if possible, 
        # OR just leave print_path as is and add the new methods.
        # The user's prompt asked for "displaying graph and shortest path", so returning the list is key.
        # reconstructing the textual print from the list loses the 'cumulative cost' per node visual unless we recalculate.
        # But `print_path` implementation I already wrote uses `curr = target ... curr = curr.parent`.
        # I will just replace `print_path` with a wrapper around `get_shortest_path` or leave it alone.
        # Let's LEAVE print_path alone and INSERT the new methods BEFORE it.
        pass

    def print_path(self, target_node_name):
        target = self.get_node(target_node_name)
        if target.distance == float('inf'):
            print(f"No path to {target_node_name}")
            return
        
        path = []
        curr = target
        while curr:
            path.append(f"{curr.name}({curr.distance})")
            curr = curr.parent
        print(f"Shortest path to {target_node_name}: {' <- '.join(path)}")

    def display(self):
        for node, neighbors in self.adj_list.items():
            # Format neighbors to show name and cost
            formatted_neighbors = [(n.name, cost) for n, cost in neighbors]
            print(f"{node.name} -> {formatted_neighbors}")

# Example Usage
if __name__ == "__main__":
    g = DirectedGraph()
    # Read from file if it exists, otherwise use hardcoded example
    try:
        print("Reading from graph_data.txt...")
        g.read_from_file("graph_data.txt")
    except FileNotFoundError:
        print("File not found, using hardcoded example.")
        g.add_edge('A', 'B', 1.0)
        g.add_edge('A', 'C', 2.0)
        g.add_edge('B', 'D', 4.0)
        g.add_edge('C', 'D', 1.0)
        g.add_edge('D', 'A', 3.0) 
    
    print("Adjacency List:")
    g.display()
    
    # Run Dijkstra
    start_node = '1'
    target_node = '2'
    print(f"\nRunning Dijkstra from {start_node}...")
    try:
        g.dijkstra(start_node)
        g.print_path(target_node)
    except Exception as e:
        print(f"Error running Dijkstra: {e}")
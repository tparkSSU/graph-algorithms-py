from functools import total_ordering

class Node:
    def __init__(self, name):
        self.name = name
        self.distance = float('inf')  # Initialize with infinity
        self.visited = False
        self.parent = None            # To reconstruct the path later

    # This method allows the heap to compare nodes: node1 < node2
    def __lt__(self, other):
        return self.distance < other.distance

    def __repr__(self):
        return f"Node({self.name}, {self.distance})"

if __name__ == "__main__":
    # verification script
    n1 = Node("A")
    n2 = Node("B")
    n1.distance = 5
    n2.distance = 10
    
    print(f"n1: {n1}")
    print(f"n2: {n2}")
    print(f"n1 < n2: {n1 < n2}") # Should be True
    print(f"n2 < n1: {n2 < n1}") # Should be False

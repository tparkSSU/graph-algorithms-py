class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insert(self, key):
        """Add a new element to the heap."""
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        """Remove and return the smallest element."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Save the root (min value)
        root = self.heap[0]
        # Move the last element to the root
        self.heap[0] = self.heap.pop()
        # Restore heap property
        self._bubble_down(0)
        return root

    def _bubble_up(self, i):
        # Move the element up until the heap property is restored
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap with parent
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def _bubble_down(self, i):
        # Move the element down until the heap property is restored
        n = len(self.heap)
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest == i:
                break
            
            # Swap with the smallest child
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

if __name__ == "__main__":
    h = MinHeap()
    data = [12, 5, 20, 2, 8, 15]
    print(f"Inserting: {data}")
    for x in data:
        h.insert(x)
    
    print(f"Heap array: {h.heap}")
    
    print("Extracting min:")
    while h.heap:
        print(h.extract_min(), end=" ")
    print()

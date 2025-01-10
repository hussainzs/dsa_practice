
"""
   Min-Heap: In a min-heap, for any given node I, the value of I is less than or equal to the values of its children. 
   The minimum element is at the root. 
"""

class Heap:
    def __init__(self):
        # Initialize the heap
        self.heap = []

    def insert(self, element):
        # Insert an element into the heap
        self.heap.append(element)
        self.heapify_up(len(self.heap) - 1)

    def delete(self):
        # Delete the root element from the heap
        pass

    def heapify_up(self, index):
        # Heapify up to maintain heap property
        pass

    def heapify_down(self, index):
        # Heapify down to maintain heap property
        pass

    def get_min(self):
        # Get the minimum element (for min-heap)
        return self.heap[0]

    def get_max(self):
        # Get the maximum element (for max-heap)
        pass

    def size(self):
        # Return the size of the heap
        pass

    def is_empty(self):
        # Check if the heap is empty
        return len(self.heap) == 0
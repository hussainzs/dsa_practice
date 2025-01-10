from math import floor
"""
   Min-Heap: In a min-heap, for any given node I, the value of I is less than or equal to the values of its children. 
   The minimum element is at the root. 
   
   Implementation of complete binary tree heap as an Array: 
   Why Use an Array?
   Space Efficiency: we don't need pointers for child or parent nodes.
   Cache Performance: Arrays benefit from better cache locality, leading to faster access times.
   
   To implement Heap using array (without Node object) we need instant access to parent, left child and right child.
   To come up with a technique for this intuitively, Let's assign indices to each node in the tree as we traverse it level by level from left to right.
        0
      /   \
     1     2
    / |   / \
   3  4  5   6
    parent = floor((index - 1) / 2)
    left_child = 2*index + 1
    right_child = 2*index + 2 
   
"""

class Heap:
    def __init__(self, contents: list[int] | None = None ):
        # Initialize the heap storage
        self.heap: list[int] = []
        
        # TODO: add contents 
    
    ### Define helper methods to implement class methods
    def getParent(self, index: int) -> int:
        if not self._hasParent(index):
            raise ValueError("Parent does not exist")
        parentIndex: int = floor((index - 1) / 2)
        return self.heap[parentIndex]
    
    def getLeftChild(self, index: int) -> int:
        leftChildIndex: int = 2 * index + 1
        return self.heap[leftChildIndex]
    
    def getrightChild(self, index: int) -> int:
        rightChildIndex: int = 2 * index + 2
        return self.heap[rightChildIndex]
    
    def _hasParent(self, index: int) -> bool:
        parentIndex: int = floor((index - 1) / 2)
        # parent index has to be greater than 0
        return parentIndex >= 0
    
    def _hasLeftChild(self, index: int) -> bool:
        leftChildIndex: int = 2 * index + 1
        # left child index has to be less than the size
        return leftChildIndex < len(self.heap)
    
    def _hasRightChild(self, index: int) -> bool:
        rightChildIndex: int = 2 * index + 2
        # right child index has to be less than the size
        return rightChildIndex < len(self.heap)
    
    def _isValidIndex(self, index: int) -> bool:
        return index < len(self.heap) and index >= 0
    
    def _swap(self, index1: int, index2: int) -> None:
        """Swaps the content of two indices inside the heap"""
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
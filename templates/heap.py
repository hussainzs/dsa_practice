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
        
    def insert(self, element: int) -> None:
        if element is None:
            raise ValueError("Can not insert None into heap")
        
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1) # heapify up the element we just inserted
        
    def _heapify_up(self, index: int) -> None:
        while self._hasParent(index):
            parentIndex = self._getParentIndex(index)
            # Swap and bubble up if parent is greater (for min heap the parent should be smaller than children)
            if self.heap[parentIndex] > self.heap[index]:
                self._swap(index, parentIndex)
                index = parentIndex
            else:
                break
    
    def _heapify_down(self, index: int) -> None:
        """Places the given index element into the correct place in the heap by bubbling it DOWN!!"""
        # if there is no left child there is definitely no right child as we are simulating complete binary tree
        while self._hasLeftChild(index):
            if self._hasRightChild(index) and self.getRightChild(index) < self.getLeftChild(index):
                minChildIndex = self._getRightChildIndex(index)
            else:
                minChildIndex = self._getLeftChildIndex(index)
            
            if self.heap[minChildIndex] < self.heap[index]:
                # 
                self._swap(index, minChildIndex)
                index = minChildIndex # and update index for next loop iteration
            else:
                break # children are smaller so we can't bubble down anymore
                
    
    ### Define helper methods
    def getParent(self, index: int) -> int:
        if not self._hasParent(index) and not self._isValidIndex(index):
            raise ValueError(f"Parent does not exist for the index {index}")
        parentIndex: int = self._getParentIndex(index)
        return self.heap[parentIndex]
    
    def getLeftChild(self, index: int) -> int:
        if not self._hasLeftChild(index) and not self._isValidIndex(index):
            raise ValueError(f"Left Child does not exist for the index {index}")
        leftChildIndex: int = self._getLeftChildIndex(index)
        return self.heap[leftChildIndex]
    
    def getRightChild(self, index: int) -> int:
        if not self._hasRightChild(index) and not self._isValidIndex(index):
            raise ValueError(f"Right child does not exist for the index {index}")
        rightChildIndex: int = self._getRightChildIndex(index)
        return self.heap[rightChildIndex]
    
    ### Internal Methods
    def _getLeftChildIndex(self, index: int) -> int:
        return 2 * index + 1
    
    def _getRightChildIndex(self, index: int) -> int:
        return 2 * index + 2
    
    def _getParentIndex(self, index: int) -> int:
        return floor((index - 1) / 2)
    
    def _hasParent(self, index: int) -> bool:
        # parent index has to be greater than 0
        return self._getParentIndex(index) >= 0
    
    def _hasLeftChild(self, index: int) -> bool:
        # left child index has to be less than the size
        return self._getLeftChildIndex(index) < len(self.heap)
    
    def _hasRightChild(self, index: int) -> bool:
        # right child index has to be less than the size
        return self._getRightChildIndex(index) < len(self.heap)
    
    def _isValidIndex(self, index: int) -> bool:
        return index < len(self.heap) and index >= 0
    
    def _swap(self, index1: int, index2: int) -> None:
        """Swaps the content of two indices inside the heap"""
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1] 
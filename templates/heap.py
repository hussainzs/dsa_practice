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
        
        if contents is not None:
            self.build_heap(contents) 
        
    def insert(self, element: int) -> None:
        if element is None:
            raise ValueError("Can not insert None into heap")
        
        self.heap.append(element)
        self._heapify_up(self.heapSize() - 1) # heapify up the element we just inserted
        
    def extract_min(self) -> int | None:
        """Extracts and returns the minimum element from the heap"""
        if self.heapSize() == 0:
            return None
        
        # store min to return later
        min: int = self.heap[0]
        
        # step 1: place the last element in the heap on the head
        self.heap[0] = self.heap[self.heapSize() - 1]
        # step 2: delete the last element
        self.heap.pop()
        # step 3: heapify down
        self._heapify_down(0)
        
        return min # return the stored min

    def _heapify_up(self, index: int) -> None:
        while self._hasParent(index):
            parentIndex = self._getParentIndex(index)
            # Swap and bubble up if parent is bigger (for min heap the parent should be smaller than children)
            if self.heap[parentIndex] > self.heap[index]:
                self._swap(index, parentIndex)
                index = parentIndex
            else:
                break
    
    def _heapify_down(self, index: int) -> None:
        """Places the given index element into the correct place in the heap by bubbling it DOWN!!"""
        # if there is no left child there is definitely no right child as we are simulating complete binary tree
        while self._hasLeftChild(index):
            # check if right child exists and if its smaller than the left child
            if self._hasRightChild(index) and self.getRightChild(index) < self.getLeftChild(index):
                minChildIndex = self._getRightChildIndex(index)
            else:
                # otherwise we know left child exists for sure because of the while condition so set that as min
                minChildIndex = self._getLeftChildIndex(index)
            
            # if child is smaller then bubble down (larger values go down, smaller goes up)
            if self.heap[minChildIndex] < self.heap[index]:
                self._swap(index, minChildIndex)
                index = minChildIndex # and update index for next loop iteration
            else:
                # children are greater or equal so we can't bubble down anymore (current value is smaller so can't go down)
                break 
    
    def build_heap(self, contents: list[int]) -> list[int]:
        """Builds in O(n) because we don't run heapify on the leaves"""
        if len(contents) == 0:
            raise ValueError("Can not build heap from empty array")
        
        self.heap = contents[:] # copy over the contents to heap for now
        
        # calculate the last parent which is half way through - 1 for the index
        lastParentIndex: int = self.heapSize() // 2 - 1
        
        # loop backwards from the last parent calling heapify on all
        for i in range(lastParentIndex, -1, -1):
            self._heapify_down(i)
            
        return self.heap
            
    ### Define helper methods
    def getParent(self, index: int) -> int:
        if not self._hasParent(index) and not self._isValidIndex(index):
            raise ValueError(f"Parent does not exist for the index {index}")
        
        return self.heap[self._getParentIndex(index)]
    
    def getLeftChild(self, index: int) -> int:
        if not self._hasLeftChild(index) and not self._isValidIndex(index):
            raise ValueError(f"Left Child does not exist for the index {index}")

        return self.heap[self._getLeftChildIndex(index)]
    
    def getRightChild(self, index: int) -> int:
        if not self._hasRightChild(index) and not self._isValidIndex(index):
            raise ValueError(f"Right child does not exist for the index {index}")

        return self.heap[self._getRightChildIndex(index)]
    
    def heapSize(self) -> int:
        return len(self.heap)
    
    def is_empty(self) -> bool:
        return self.heapSize() == 0
    
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
        return self._getLeftChildIndex(index) < self.heapSize()
    
    def _hasRightChild(self, index: int) -> bool:
        # right child index has to be less than the size
        return self._getRightChildIndex(index) < self.heapSize()
    
    def _isValidIndex(self, index: int) -> bool:
        return index < self.heapSize() and index >= 0
    
    def _swap(self, index1: int, index2: int) -> None:
        """Swaps the content of two indices inside the heap"""
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1] 
        
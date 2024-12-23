from typing import Any, Optional

# Node 
class Node:
    def __init__(self, value: Any,
                 prev: Optional['Node'] = None, 
                 next: Optional['Node'] = None
                 ) -> None:
        self.value: Any = value
        self.prev: Optional['Node'] = prev
        self.next: Optional['Node'] = next
        
    # define getters 
    def getValue(self) -> Any:
        return self.value
    
    def getPrev(self) -> Optional['Node']:
        return self.prev

    def getNext(self) -> Optional['Node']:
        return self.next
    
    #-------
    
    #define setters
    def setValue(self, newValue: Any) -> None:
        self.value = newValue
    
    def setPrev(self, newPrev: Optional['Node']) -> None:
        self.prev = newPrev
        
    def setNext(self, newNext: Optional['Node']) -> None:
        self.next = newNext
        

# Doubly LinkedList Class 
class DoubleLinkedList:
    def __init__(self, contents: list[Any] = []) -> None:
        self.first: Node = Node(None, prev=None, next=None) #Dummy Node
        self.last: Node = self.first
        self.length: int = 0
        
        #initialize the list with values given in contents array
        for c in contents:
            self.append(c)
        
    def append(self, val: Any) -> None:
        currentLast: Node = self.last  # Store the current last node from the list
        # Create a new node with the given value, setting its previous node to the current last node and next node to None
        newLastNode: Node = Node(val, prev=currentLast, next=None)  
        self.last.next = newLastNode  # Link the current last node next pointer to new last node
        self.last = newLastNode  # Update the last node reference to the new node
        self.length += 1  
        
    def get_index(self, index: int) -> Optional['Node']:
        if index < 0 or index >= self.length:
            max_valid_index: int = 0 if self.length == 0 else self.length - 1
            raise IndexError(f"Index out of bounds, max valid index was {max_valid_index}")
        
        curr_node: Optional['Node'] = self.first.getNext()
        for _ in range(index):
            if curr_node is not None:
                curr_node = curr_node.getNext()
        return curr_node
            
        
        

# Problems 

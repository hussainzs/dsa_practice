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
    def _getValue(self) -> Any:
        return self.value
    
    def _getPrev(self) -> Any:
        return self.prev

    def _getNext(self) -> Any:
        return self.next
    
    #-------
    
    #define setters
    def _setValue(self, newValue: Any) -> None:
        self.value = newValue
    
    def _setPrev(self, newPrev: Optional['Node']) -> None:
        self.prev = newPrev
        
    def _setNext(self, newNext: Optional['Node']) -> None:
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
        currentLast: Node = self.last
        newLastNode: Node = Node(val, prev=currentLast, next=None)
        self.last.next = newLastNode
        self.last = newLastNode
        
        

# Problems 

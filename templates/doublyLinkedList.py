from turtle import right
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
        self.last.setNext(newLastNode) # Link the current last node next pointer to new last node
        self.last = newLastNode  # Update the last node reference to the new node
        self.length += 1  
        
    def get_node_at_index(self, index: int) -> Node:
        if index < 0 or index >= self.length:
            max_valid_index: int = 0 if self.length == 0 else self.length - 1
            raise IndexError(f"Index out of bounds, max valid index was {max_valid_index}")
        
        curr_node: Optional['Node'] = self.first.getNext()
        for _ in range(index):
            if curr_node is not None:
                curr_node = curr_node.getNext()
        assert curr_node is not None, "This method must return valid Node, for invalid index it raises IndexError"
        return curr_node
    
    def set_val_at_index(self, index: int, val: Any) -> None:
        current_node: Node = self.get_node_at_index(index)
        current_node.setValue(val)
        
    def remove_at_index(self, index: int) -> int:
        """Removes the Node at given index. Adjusts the attached pointers to deleted node.

        Args:
            index (int): index in the list where node has to be deleted

        Returns:
            int: updated length after removal
        """
        node_to_remove: Node = self.get_node_at_index(index)
        
        # Get left and right of the node to remove
        node_before_target: Optional['Node'] = node_to_remove.getPrev() # left of the desired node
        assert node_before_target is not None # if get_node_at_index didn't throw an error we have a valid index which has a Node on the left for sure
        node_after_target: Optional['Node'] = node_to_remove.getNext() # right of the desired node
        
        # Update neighboring links        
        node_before_target.setNext(node_after_target) # next pointer of left -> right
        # if we were removing the last node (i.e. Node after target is None)
        if node_after_target is None: 
            self.last = node_before_target # update the reference to last node but don't set prev pointer
        else:
            node_after_target.setPrev(node_before_target) # prev pointer of right to left
            
        # Help garbage collector by setting item to be removed to none
        node_to_remove.setNext(None)
        node_to_remove.setPrev(None)
        node_to_remove.setValue(None)
                   
        self.length -= 1
        return self.length  
            
        
        

# Problems 

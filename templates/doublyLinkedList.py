from dataclasses import dataclass, field
from typing import Any, Optional

@dataclass
class Node:
    value: Any
    prev: Optional['Node'] = field(default=None)
    next: Optional['Node'] = field(default=None)
    
class DoublyLinkedList:
    def __init__(self, contents: list[Any] | None = None) -> None:
        self.head: Node = Node(value=None, prev=None, next=None)
        self.tail: Node = self.head
        self.size: int = 0
        
        if contents is not None:
            for c in contents:
                self.append(c)
    
    def append(self, value: Any) -> None:
        """Appends a new element to the end of the doubly linked list

        Args:
            value (Any): value to be appended

        Raises:
            TypeError: Null/None values can not be appended/added to the list.
        """
        if value is None:
            raise TypeError("None/Null value can not be inserted")
        
        new_node: Node = Node(value=value, prev=self.tail, next=None) # initializze new tail
        self.tail.next = new_node # set current tail's next pointer to new tail
        self.tail = new_node # update our tail pointer to new tail
        self.size += 1 # increment size by 1
        
    def get_value_at_index(self, index: int) -> Node:
        if index is None:
            raise IndexError("Index can not be None")
        if index < 0 or index > self.size - 1:
            raise IndexError(f"Index out of bounds, max valid index is {self.size - 1}")
        
        current_node: Optional["Node"] = self.head.next # get first valid node (maybe none if list empty)
        for _ in range(index):
            if current_node is not None: # if current_node none then .next does not exist so we must check
                current_node = current_node.next
        assert current_node is not None, "can not return None, something went wrong in the get method"
        return current_node
            
        
        
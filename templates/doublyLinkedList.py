from dataclasses import dataclass, field
from typing import Any, Optional

@dataclass
class Node:
    value: Any
    prev: Optional['Node'] = field(default=None)
    next: Optional['Node'] = field(default=None)
    
class DoublyLinkedList:
    def __init__(self, contents: list[Any] | None = None) -> None:
        self._head: Node = Node(value=None, prev=None, next=None)
        self._tail: Node = self._head
        self._size: int = 0
        
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
        
        new_node: Node = Node(value=value, prev=self._tail, next=None) # initializze new tail
        self._tail.next = new_node # set current tail's next pointer to new tail
        self._tail = new_node # update our tail pointer to new tail
        self._size += 1 # increment size by 1
        
    def get_value_at_index(self, index: int) -> Node:
        """Get the node at specified index. Equivalent to a normal list indexing like arr[index]

        Args:
            index (int): index to retrieve node at

        Raises:
            IndexError: if index is None
            IndexError: if index is negative or greater than self.size - 1 which is max valid index for any list

        Returns:
            Node: Node at the specified index
        """
        if index is None:
            raise IndexError("Index can not be None")
        if index < 0 or index > self._size - 1: # remember size - 1 is the highest valid index
            raise IndexError(f"Index out of bounds, max valid index is {self._size - 1}")
        
        current_node: Optional["Node"] = self._head.next # get first valid node (maybe none if list empty)
        for _ in range(index): 
            if current_node is not None: # if current_node none then .next does not exist so we must check
                current_node = current_node.next # move to next node in the chain
        assert current_node is not None, "can not return None from get method in this implementation"
        return current_node
    
    def set_value_at_index(self, value: Any, index: int) -> None:
        """Set value at a valid index

        Args:
            value (Any): value to be updated
            index (int): index at which the node exists

        Raises:
            TypeError: value can not be None
        """
        if value is None:
            raise TypeError("None/Null value can not be set")
        node_to_update: Node = self.get_value_at_index(index)
        node_to_update.value = value
    
    def remove_at_index(self, index: int) -> int:
        """Removes node at a valid index. Will throw error if index is invalid using the error checking of get method

        Args:
            index (int): Index to remove Node from

        Returns:
            int: remaining size of the list after removal
        """
        node_to_remove: Node = self.get_value_at_index(index)
        prev_node: Node # node to the left of node we want to remove
        next_node: Optional['Node'] = node_to_remove.next # this can be None (if remvoing the last element)
        if index == 0: # if removing the first element, the prev node is dummy node
            prev_node = self._head # we can't use get method here becuase we will have to pass invalid index
        else:
            prev_node = self.get_value_at_index(index-1) 
        
        if next_node is None: # if removing last node then next_node is None
            self._tail = prev_node # therefore, update tail pointer to prev_node (this maybe dummy node in case there was only 1 element)
        else:
            next_node.prev = prev_node # here next_node can never be null thus set its prev pointer to prev_node

        # always update the prev_node's next pointer to next_node (even if its None it makes sense because dummy node exists)
        prev_node.next = next_node 
        
        # just to help garbage collector
        del(node_to_remove)
        
        # update size
        self._size -= 1
        return self._size
     
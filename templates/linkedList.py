from dataclasses import field, dataclass
from typing import Optional, Any

@dataclass
class Node:
    value: Any
    next: Optional['Node'] = field(default=None)

class LinkedList:
    def __init__(self, contents: list[Any] | None = None) -> None:
        self.head: Node = Node(value=None, next=None) # set head to a dummy node
        self.tail: Node = self.head
        self.size: int = 0
        
        if contents is not None:
            for c in contents:
                self.append(c)
    
    def append(self, val: Any) -> None:
        if val is None:
            raise TypeError("Can not append a value of None into this LinkedList")
        newTailNode: Node = Node(value=val, next=None)
        self.tail.next = newTailNode
        self.tail = newTailNode
        self.size += 1
    
    def get_value_at_index(self, index: int) -> Node:
        if index < 0 or index >= self.size:
            raise IndexError(f"Index out of bounds, max valid index is {self.size - 1}")
        curr_node: Optional['Node'] = self.head.next # first valid node
        for _ in range(index):
            if curr_node is not None:
                curr_node = curr_node.next
        assert curr_node is not None, "can not access invalid index in this implementation"
        return curr_node
    
    def set_value_at_index(self, index: int, val: Any) -> None:
        if val is None:
            raise TypeError("Can not append a value of None into this LinkedList")
        node_to_update: Node = self.get_value_at_index(index)
        node_to_update.value = val
        
    def remove_at_index(self, index: int) -> int:
        """Remove node at given index from the list. 

        Args:
            index (int): index of node to be removed

        Returns:
            int: the size (num of itens) of the list AFTER the removal
            
        Raises:
            IndexError: if index < 0 or index >= size
        """
        # check if valid index is requeested to remove
        node_to_remove: Node = self.get_value_at_index(index)
        prev_node: Node # Node prev to the one we want to remove
        if index == 0: # if removing the first item then prev is dummy node
            prev_node = self.head
        else:
            prev_node = self.get_value_at_index(index - 1)
        # if removing the last item then update tail to be its prev node
        if index == self.size - 1:
            self.tail = prev_node
        # adjust the links from prev
        prev_node.next = node_to_remove.next
        self.size -= 1 # decrement size by 1 after successful removal
        return self.size
        
        
        
        
            
    
        
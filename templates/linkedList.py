from dataclasses import field, dataclass
from typing import Optional, Any


@dataclass
class Node:
    value: Any
    next: Optional['Node'] = field(default=None)


class LinkedList:
    def __init__(self, contents: list[Any] | None = None) -> None:
        self._head: Node = Node(value=None, next=None)  # set head to a dummy node
        self._tail: Node = self._head
        self._size: int = 0

        if contents is not None:
            for c in contents:
                self.append(c)

    def append(self, val: Any) -> None:
        if val is None:
            raise TypeError("Can not append a value of None into this LinkedList")
        new_tail_node: Node = Node(value=val, next=None)
        self._tail.next = new_tail_node
        self._tail = new_tail_node
        self._size += 1

    def get_value_at_index(self, index: int) -> Node:
        if index is None:
            raise IndexError("Index can not be None")
        if index < 0 or index >= self._size:
            raise IndexError(f"Index out of bounds, max valid index is {self._size - 1}")
        curr_node: Optional['Node'] = self._head.next  # first valid node
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
            int: the size (num of items) of the list AFTER the removal
            
        Raises:
            IndexError: if index < 0 or index >= size
        """
        # check if valid index is requested to remove
        node_to_remove: Node = self.get_value_at_index(index)
        prev_node: Node  # Node prev to the one we want to remove
        if index == 0:  # if removing the first item then prev is dummy node
            prev_node = self._head
        else:
            prev_node = self.get_value_at_index(index - 1)
        # if removing the last item then update tail to be its prev node
        if index == self._size - 1:
            self._tail = prev_node
        # adjust the links from prev
        prev_node.next = node_to_remove.next
        self._size -= 1  # decrement size by 1 after successful removal
        return self._size
    
    def get_head(self) -> Any:
        """Returns the head of the list. Helpful for Queue implementation

        Returns:
            Any: Value at the head (front) of the linkedlist
        """
        return self._head.value
    
    def remove_head(self) -> None:
        """Removes the head of the list. Throws assertion error if list is empty
        Helpful in Queue implementation
        
        Returns:
            None
        """
        assert self._head.next is not None, "Can not remove head from empty linked list"
        
        current_first: Node = self._head.next # get the head (remember that's next of dummy node which is always the head)
        
        if current_first == self._tail: # if there is only one Node in list (which will be the tail)
            self._tail = self._head # update the tail to dummy head since that one item is about to be removed
        
        self._head.next = current_first.next # set the dummy head's next to whatever comes after current_first
        del(current_first)
        
    def get_size(self) -> int:
        return self._size
        
            
        
        

from typing import Any

class Stack:
    def __init__(self, contents: list[Any] | None = None) -> None:
        """
        Initialize a new stack.
        Args:
            contents (list[Any] | None): Optional initial contents of the stack. 
                                         If provided, each element will be pushed onto the stack.
        Returns:
            None
        """
        self.stack: list[Any] = []
        
        if contents is not None:
            for c in contents:
                self.push(c)
    
    def push(self, item: Any) -> None:
        """
        Push an item onto the stack.

        Args:
            item (Any): The item to be pushed onto the stack. Must not be None.

        Raises:
            AssertionError: If the item is None.
        """
        assert item is not None, "Can not push Null into stack"
        self.stack.append(item)
    
    def pop(self) -> Any:
        """
        Remove and return the top item from the stack.
        Raises:
            IndexError: If the stack is empty.
        Returns:
            Any: The item that was removed from the stack.
        """
        if self.is_empty():
            raise IndexError("Can not pop from an empty stack")
        
        last_index: int = len(self.stack) - 1
        item: Any = self.stack[last_index]
        del(self.stack[last_index])
        return item
                
    def peek(self) -> Any:
        """
        Return the top element of the stack without removing it.

        Returns:
            Any: The top element of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Can not peek from an empty stack")
        return self.stack[len(self.stack) - 1]
    
    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0
        
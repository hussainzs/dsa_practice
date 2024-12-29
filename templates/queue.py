from typing import Any
from linkedList import LinkedList

class Queue:
    def __init__(self, contents: list[Any] | None = None) -> None:
        if contents is not None:
            self.queue = LinkedList(contents=contents)
        else:
            self.queue = LinkedList()
    
    def enqueue(self, item: Any) -> None:
        assert item is not None, "Can not enqueue Null item into the Queue"
        self.queue.append(item)
    
    def peek (self) -> Any:
        self.queue.get_head()
    
    def is_empty(self) -> bool:
        return self.queue.get_size() == 0
    
    def dequeue(self) -> Any:
        self.queue.remove_head()
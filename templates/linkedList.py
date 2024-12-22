from logging import raiseExceptions
from typing import Any, Optional

from argon2 import Type

class Node:
    """
    A class used to represent a Node in a linked list.
    Attributes
    ----------
    item : Any
        The data stored in the node.
    next : Optional['Node']
        The reference to the next node in the linked list, or None if it is the last node.
    """
    # Optional[X] is equivalent to Union[X, None]
    # we set optional for next beacuse some nodes won't have next i.e. last one
    def __init__(self, item: Any, next: Optional['Node'] = None) -> None:
        self.item = item 
        self.next = next
        
    def getItem(self) -> Any:
        return self.item
    
    def getNext(self) -> Optional['Node']:
        return self.next
    
    def setItem(self, item_input: Any) -> Any:
        self.item = item_input
        return self.item
    
    def setNext(self, next_input: Optional['Node']) -> Optional['Node']:
        self.next = next_input
        return self.next
    

"""
For our LinkedList we will keep track of 3 things 
1. reference to first node (always a dummy variable who's next pointer will be set to the first value of the list)
2. reference to last node [enables O(1) insertion at the end]
3. number of items (size of the list)
"""

class LinkedList:
    def __init__(self, contents: list[Any] = []) -> None:
        # first define a dummy node with none item and none reference
        self.first: Node = Node(None, None)
        self.last: Node = self.first
        self.numitems: int = 0
        
        # TODO: if at initiatization, list content was provided then add this to the list starting from dummy
        for c in contents:
            self.append(c)
        
    def append(self, item: Any) -> None:
        if item is None:
            raise TypeError(f"Expected non-null values, recieved Null/None")
        
        nextNode: Node = Node(item, None) # initialize a Node 
        self.last.setNext(next_input=nextNode) # redirect the current last node to next Node
        self.last = nextNode # update our pointer of last node to next Node
        
        
        
        
        
        

"""
Possible Questions:
Q1. HOW DID YOU HANDLE APPENDING NULL VALUES OR EMPTY VALUES?
Ans: In this implementation, I returned an error. But depends on the design choice

Q2. HOW WOULD YOU ENFORCE THAT SAME TYPE OF DATA IS INSERTED IN THE LIST?
Ans: I would store the data type as an internal attribute i.e. `self._data_type` and raise validation errors in methods
"""
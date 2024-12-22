from typing import Any, Optional

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
        self.first: Optional['Node'] = Node(None, None)
        self.last: Optional['Node'] = self.first
        self.numitems: int = 0
        
        # TODO: if at initiatization, list content was provided then add this to the list starting from dummy
        
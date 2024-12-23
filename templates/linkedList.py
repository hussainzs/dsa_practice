from turtle import right
from typing import Any, Optional

class Node:
    """
    Node for linkedlist

    Attributes
    ----------
    item : Any
        The data stored in the node.
    next : Optional['Node']
        The reference to the next node in the linked list, or None if it is the last node.
    """
    def __init__(self, item: Any, next: Optional['Node'] = None) -> None:
        """
        Initializes a new node with the given item and next node reference.

        Parameters
        ----------
        item : Any
            The data stored in the node.
        next : Optional['Node'], optional
            The reference to the next node in the linked list, by default None.
        """
        self.item = item 
        self.next = next
        
    def getItem(self) -> Any:
        """
        Returns the item stored in the node.

        Returns
        -------
        Any
            The data stored in the node.
        """
        return self.item
    
    def getNext(self) -> Optional['Node']:
        """
        Returns the reference to the next node.

        Returns
        -------
        Optional['Node']
            The reference to the next node, or None if it is the last node.
        """
        return self.next
    
    def setItem(self, item_input: Any) -> Any:
        """
        Sets the item stored in the node.

        Parameters
        ----------
        item_input : Any
            The new data to store in the node.

        Returns
        -------
        Any
            The updated data stored in the node.
        """
        self.item = item_input
        return self.item
    
    def setNext(self, next_input: Optional['Node']) -> Optional['Node']:
        """
        Sets the reference to the next node.

        Parameters
        ----------
        next_input : Optional['Node']
            The new reference to the next node.

        Returns
        -------
        Optional['Node']
            The updated reference to the next node.
        """
        self.next = next_input
        return self.next
    

class LinkedList:
    """
    Custom stricter Linkedlist

    Attributes
    ----------
    first : Node
        The reference to the first node, if empty then there exists a dummy node with None value and None next pointer
    last : Node
        The reference to the last node, enabling O(1) insertion at the end.
    numitems : int
        The number of items in the list.
    """
    def __init__(self, contents: list[Any] = []) -> None:
        """
        Initializes a new linked list with optional initial content of items.

        Parameters
        ----------
        contents : list[Any], optional
            A list of initial content to populate the linked list, by default empty array [].
        """
        self.first: Node = Node(item=None, next=None) # dummy Node 
        self.last: Node = self.first
        self.numitems: int = 0
        
        for c in contents:
            self.append(c)
            
    def append(self, item: Any) -> None:
        """
        Appends a new item to the end of the list.
        Stricter restrictions: can not insert Null values

        Parameters
        ----------
        item : Any
            The new item to append to the list.

        Raises
        ------
        AssertionError
            If the item is None.
        """
        assert item is not None, "Expected non-null values to append, received Null/None"
        
        nextNode: Node = Node(item, next=None)
        self.last.setNext(nextNode)
        self.last = nextNode
        self.numitems += 1
            
    def get_indexed_item(self, index: int) -> Node:
        """
        Retrieves the node at the specified index.

        Parameters
        ----------
        index : int
            The index of the node to retrieve.

        Returns
        -------
        Node
            The node at the specified index.

        Raises
        ------
        IndexError
            If the index is out of bounds or the list is empty.
        """
        assert index is not None, "Expected non-null index, received None"
        if index >= self.numitems or index < 0:
            max_valid_index: int = 0 if self.numitems == 0 else self.numitems - 1
            if max_valid_index == 0:
                raise IndexError("List is empty, cannot get values from empty list")
            else:
                raise IndexError(f"Index out of bounds, max valid index is {max_valid_index}")
            
        current_node: Optional['Node'] = self.first.getNext()
        for _ in range(index):
            if current_node is not None: 
                current_node = current_node.getNext()
        assert current_node is not None, "This strict method can't return None"
        return current_node
    
    def set_indexed_item(self, index: int, newItem: Any) -> None:
        """
        Sets a value at the given index in the list. Equivalent to list[index] = newItem

        Parameters
        ----------
        index : int
            The index at which to set the new value.
        newItem : Any
            The new value to set at the specified index.

        Raises
        ------
        IndexError
            If the index is out of bounds.
        """
        assert newItem is not None, "Expected non-null value to set, received None"
        current_node: Node = self.get_indexed_item(index)
        current_node.setItem(newItem)
    
    def remove_at_index(self, index: int) -> int:
        """
        Removes the node at specified index and adjusts the pointers of its neighbors
        
        Parameters
        ----------
        index: int 
            The index of node to be removed
        
        Returns
        -------
        int
            remaining length of list after removal
        """
        node_to_remove: Node = self.get_indexed_item(index)
        # we know there will always be a left node at index - 1 because of the dummy node 
        # and because we only execute this if get_indexed_item above didn't raise an error 
        # which means the index is valid.
        left_node: Node = self.get_indexed_item(index - 1)
        # but we may not have a right node (it might be None) because we may be removing the last item
        right_node: Optional['Node'] = node_to_remove.getNext()
        
        # Adjust the links from left to right
        left_node.setNext(right_node)
        
        # Help garbage collector by setting its links to none
        node_to_remove.setNext(None)
        
        self.numitems -= 1
        return self.numitems
        
    
        
        
"""
Possible Questions:
Q1. HOW DID YOU HANDLE APPENDING NULL VALUES OR EMPTY VALUES?
Ans: In this implementation, I returned an error. But depends on the design choice

Q2. HOW WOULD YOU ENFORCE THAT SAME TYPE OF DATA IS INSERTED IN THE LIST?
Ans: I would store the data type as an internal attribute i.e. `self._data_type` and raise validation errors in methods
"""
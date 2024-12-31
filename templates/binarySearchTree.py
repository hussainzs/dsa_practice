from dataclasses import dataclass, field
from typing import Optional

@dataclass
class BSTNode:
    value: int
    right: Optional['BSTNode'] = field(default=None)
    left: Optional['BSTNode'] = field(default=None)


class BinarySearchTree:
    def __init__(self, contents: list[int] | None = None) -> None:
        self.root: Optional[BSTNode] = None
        
        #TODO: handle contents array

    def insert(self, val: int) -> BSTNode:
        """Inserts a integer into BST. 

        Args:
            val (int): integer to be inserted

        Raises:
            TypeError: Can not insert None values into BST

        Returns:
            BSTNode: Returns the root of the tree
        """
        if val is None:
            raise TypeError("Can not insert None value into Binary Search Tree")
        
        # we will call this recursive method starting from root
        def __insert_recursive(curr: Optional['BSTNode'], val: int) -> BSTNode:
            # Base Case:
            if curr is None:
                return BSTNode(value=val, right=None, left=None)
            if val >= curr.value:
                curr.right = __insert_recursive(curr.right, val)
            else:
                # val < curr.value
                curr.left = __insert_recursive(curr.left, val)
            return curr
            
        self.root = __insert_recursive(self.root, val)
        return self.root
            

    def search(self, val: int) -> Optional[BSTNode]:
        pass

    def delete(self, val: int) -> None:
        pass

    def find_min(self) -> Optional[int]:
        pass

    def find_max(self) -> Optional[int]:
        pass

    def is_empty(self) -> bool:
        return False
    
    def inorder_traversal(self) -> list[int]:
        return []

    def preorder_traversal(self) -> list[int]:
        return []

    def postorder_traversal(self) -> list[int]:
        return []
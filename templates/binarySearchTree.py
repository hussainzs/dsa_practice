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
        self.num_nodes: int = 0
        
        if contents is not None:
            for c in contents:
                self.insert(c)

    def insert(self, val: int) -> BSTNode:
        """Inserts a integer into BST. Increments the num_nodes as well

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
                self.num_nodes += 1
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
        """Finds and returns the Node that contains the desired value. Returns None if not found
        In case of duplicates, it finds the first instance.

        Args:
            val (int): value to be found.

        Returns:
            Optional[BSTNode]: The node containing the value
        """
        if val is None:
            raise TypeError("Can not search for None in BST")
        
        if self.num_nodes == 0:
            return None # there is nothing to search in an empty BST
        
        def __search_recursive(curr: Optional['BSTNode']) -> Optional[BSTNode]:
            if curr is None:
                return None # couldn't find the desired node
            elif curr.value == val:
                return curr # return the desired node since we found it
            elif val >= curr.value:
                return __search_recursive(curr.right) # explore right subtree
            else:
                return __search_recursive(curr.left) # explore left subtree
        return __search_recursive(self.root)
        

    def delete(self, val: int) -> None:
        pass

    def find_min(self) -> Optional[int]:
        pass

    def find_max(self) -> Optional[int]:
        pass

    def is_empty(self) -> bool:
        return self.num_nodes == 0
    
    def sum(self) -> int:
        def __sum(curr_node: Optional['BSTNode']) -> int:
            if curr_node is None:
                return 0
            left_sum: int = __sum(curr_node.left)
            right_sum: int = __sum(curr_node.right)
            return curr_node.value + left_sum + right_sum
        return __sum(self.root)
            
    
    def inorder_traversal(self) -> list[int]:
        return []

    def preorder_traversal(self) -> list[int]:
        return []

    def postorder_traversal(self) -> list[int]:
        return []
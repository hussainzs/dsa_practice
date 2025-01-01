from dataclasses import dataclass, field
from typing import Optional

from networkx import is_empty

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
        
        if self.is_empty():
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

    def find_min(self) -> int:
        """Finds the min value of the BST

        Raises:
            ValueError: If BST is Empty 

        Returns:
            int: Minimum value of the BST
        """
        if self.root is None:
            raise ValueError("Empty BST does not have any min")
        
        def __find_min(curr: BSTNode) -> int:
            curr_node: BSTNode = curr
            while (curr_node.left is not None):
                curr_node = curr_node.left
            return curr_node.value 
        
        return __find_min(self.root)
        

    def find_max(self) -> int:
        """Finds the maximum integer value in the BST

        Raises:
            ValueError: if Tree is empty

        Returns:
            int: maximum value in the BST
        """
        if self.root is None:
            raise ValueError("Empty BST does not have any max")
        
        def __find_max(node: BSTNode) -> int:
            curr_node: BSTNode = node
            while (curr_node.right is not None):
                curr_node = curr_node.right
            return curr_node.value
        
        return __find_max(self.root)

    def is_empty(self) -> bool:
        """Check if the BST is empty (no nodes)

        Returns:
            bool: True if BST is empty and False otherwise
        """
        return self.num_nodes == 0 or self.root is None
    
    def sum(self) -> int:
        """Calculates the integer sum of all values in the tree

        Returns:
            int: sum of all nodes in the BST
        """
        if self.num_nodes == 0:
            return 0
        
        def __sum(curr_node: Optional['BSTNode']) -> int:
            if curr_node is None:
                return 0
            left_sum: int = __sum(curr_node.left)
            right_sum: int = __sum(curr_node.right)
            return curr_node.value + left_sum + right_sum
        
        return __sum(self.root)
    
    def height(self) -> int:
        """
        Calculate the height of the BST.
        The height of a binary search tree is the number of edges 
        on the longest path from the root node to a leaf node. 
        An empty tree has a height of -1 
        
        Returns:
            int: The height of the tree. Returns -1 if the tree is empty.
        """
        if self.root is None:
            return -1 # height of empty tree is -1
        
        def __height(node: BSTNode) -> int:
            if node is None:
                return -1
            left_height: int = __height(node.left) if node.left is not None else 0
            right_height: int = __height(node.right) if node.right is not None else 0
            return 1 + max(left_height, right_height)
        
        return __height(self.root)
        
    def inorder_traversal(self) -> list[int]:
        """
        Performs an in-order traversal (Left -> Root -> Right) of the BST and returns a list of node values in ascending order.

        Raises:
            ValueError: If the BST is empty.

        Returns:
            list[int]: A list of node values in ascending order.

        Helpful for:
            - Generating a sorted list of the node values.
            - Checking if a tree is a BST by ensuring the in-order traversal produces a sorted sequence.
            - Finding the k-th smallest element in the BST.
            - Performing range queries to find all elements within a given range [low, high].
            - Converting the BST to a sorted doubly linked list.
        """
        if self.root is None:
            raise ValueError("Can not traverse an Empty BST")
        
        result: list[int] = []
        def __inorder(node: Optional['BSTNode']) -> None:
            if node is not None:
                __inorder(node.left) # ensures that all nodes with values less than the current node are processed first. 
                result.append(node.value)
                __inorder(node.right) # ensures that all nodes with values greater than the current node are processed last.
                
        __inorder(self.root) 
        return result

    
    def postorder_traversal(self) -> list[int]:
        """Performs a post-order traversal (Left -> Right -> Root) of the BST and returns a list of values. Children are traversed first

        Raises:
            ValueError: If BST is empty

        Returns:
            list[int]: A list of node values in post-order
        """
        if self.root is None:
            raise ValueError("Can not traverse an Empty BST")
        
        result: list[int] = []
        def __postorder(node: Optional['BSTNode']) -> None:
            if node is not None:
                __postorder(node.left) 
                __postorder(node.right) 
                result.append(node.value)
                
        __postorder(self.root) 
        return result
    
    def delete(self, val: int) -> Optional['BSTNode']:
        if val is None:
            raise TypeError("Can not delete Null values")
        if self.is_empty():
            return None # nothing to delete in an empty tree
        
        def __delete(node: Optional['BSTNode']) -> Optional['BSTNode']:
            if node is None:
                return None
            if node.value < val:
                node.right = __delete(node.right)
            elif node.value > val:
                node.left =  __delete(node.left)
            else:
                # node.value == val so we want to delete this node
                # Case 1: node's left or right child are none
                if node.left is None: 
                    return node.right 
                elif node.right is None:
                    return node.left
                else:
                    # Case 2: node has both left and right children so we find minimum on the right to replace it
                    successor_parent: BSTNode = node
                    successor: BSTNode = node.right
                    while successor.left is not None:
                        successor_parent = successor
                        successor = successor.left
                    node.value = successor.value  # Replace node's value with successor's value

                    # Delete the inorder successor
                    # an alternative approach here will be to do this (change the method signature for this)
                    # node.right = __delete(node.right, successor.value)
                    if successor_parent.left == successor:
                        successor_parent.left = successor.right
                    else:
                        # successor_parent.right == successor (this only happens when successor is the immediate right child of the node we wanna delete)
                        successor_parent.right = successor.right
            return node
        self.root = __delete(self.root)
        return self.root
            
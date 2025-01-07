from dataclasses import dataclass, field
from typing import Optional
from collections import deque

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
    
    def delete(self, val: int) -> Optional['BSTNode']:
        """
        Deletes a node with the given value from the binary search tree.
        This approach uses a mix of iterative and recursive approach.
        Check the code comments to see the usual purely recursive approach. 
        
        Args:
            val (int): The value of the node to be deleted.
        Returns:
            Optional['BSTNode']: The root of the modified tree after deletion, or None if the tree is empty.
        Raises:
            TypeError: If the value to be deleted is None.
        The deletion process involves three main cases:
        1. The node to be deleted has no children (it is a leaf node).
        2. The node to be deleted has one child.
        3. The node to be deleted has two children. In this case, the node's value is replaced with its
        inorder successor's value, and the inorder successor is then deleted.
        The function uses a helper function `__delete` to recursively find and delete the node.
        """
        if val is None:
            raise TypeError("Can not delete Null values")
        if self.is_empty():
            return None  # Nothing to delete in an empty tree

        def __delete(node: Optional['BSTNode']) -> Optional['BSTNode']:
            if node is None:
                return None  # Base case: If the node is None, nothing can be deleted
            if node.value < val:
                # in other words: If the value to be deleted is greater than the current node's value,
                # traverse the right subtree
                node.right = __delete(node.right)
            elif node.value > val:
                # If the value to be deleted is less than the current node's value,
                # traverse the left subtree
                node.left = __delete(node.left)
            else:
                # Node to be deleted is found
                # Case 1: Node has no left child (this covers the scenario where both children are none)
                if node.left is None:
                    return node.right  # Replace node with its right child
                # Case 2: Node has no right child
                elif node.right is None:
                    return node.left  # Replace node with its left child
                else:
                    # Case 3: Node has two children
                    # Find the inorder successor (smallest/minimum node in the right subtree)
                    successor_parent: BSTNode = node # this will help us delete the successor manually without recursive call
                    successor: BSTNode = node.right
                    while successor.left is not None: # keep exploring left to find min value 
                        successor_parent = successor
                        successor = successor.left
                    node.value = successor.value # Replace the node's value with the successor's value [deletes the node]

                    # Delete the inorder successor
                    # --> an alternative approach here will be to use recursion (change the method signature for this)
                    # node.right = __delete(node.right, successor.value)
                    if successor_parent.left == successor: 
                        successor_parent.left = successor.right
                    else:
                        # This case happens when the successor is the immediate right child of the node to be deleted [i.e. successor_parent is the node we chnged the value of]
                        successor_parent.right = successor.right
            return node

        self.root = __delete(self.root)
        self.num_nodes -= 1 # decrease the number of nodes
        return self.root

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
        
        Returns:
            int: The height of the tree. Returns -1 if the tree is empty.
        """
        if self.root is None:
            return -1 # height of empty tree is -1
        
        def __height(node: BSTNode) -> int:
            if node is None:
                return 0
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
    
    def balance(self) -> BSTNode:
        """Balances the BST where the height of the left and right subtrees of any node differ by no more than one.
        
        Returns:
            BSTNode: root of balanced tree
        """   
        ascending: list[int] = self.inorder_traversal() # get the ascending list of values for the tree
        if self.is_balanced(): # if BST is already balanced we just return the current root
            assert self.root is not None
            return self.root
        
        # recursive function below assumes len(list) > 0
        def __balance_bst(ascending_values: list[int]) -> BSTNode:
            if len(ascending_values) == 1:
                return BSTNode(value=ascending_values[0], left=None, right=None)
            elif len(ascending_values) == 2:
                left_child = BSTNode(value=ascending_values[0], left=None, right=None)
                parent_node = BSTNode(value=ascending_values[1], left=left_child, right=None)
                return parent_node
            else:
                # len is atleast 3
                mid: int = len(ascending_values) // 2
                left_child = __balance_bst(ascending_values[0:mid])
                right_child =  __balance_bst(ascending_values[mid+1:])
                root_node = BSTNode(value=ascending_values[mid], left=left_child, right=right_child)
                return root_node
        self.root = __balance_bst(ascending)
        return self.root
    
    def is_balanced(self) -> bool:
        """Checks the height of the left and right subtrees of each node and ensures that the difference in height is no more than one.

        Raises:
            ValueError: If BST is empty

        Returns:
            bool: True if balanced and False otherwise
        """
        if self.is_empty():
            raise ValueError("Empty BST can not be checked for balance")
        
        def __check_balance(node: Optional['BSTNode']) -> int:
            if node is None:
                return 0
            
            left_height: int = __check_balance(node.left)
            if left_height == -1: return -1
            
            right_height: int = __check_balance(node.right)
            if right_height == -1: return -1
            
            height_diff: int = abs(left_height - right_height)
            if height_diff > 1:
                return -1
            
            return 1 + max(left_height, right_height) # calculates the height
        
        return __check_balance(self.root) != -1
    
    def bfs(self) -> list[list[int]]:
        """Returns a list of list where each list at index contains the nodes of that level.
        For example, list at index 0 contains all the nodes at level 0.

        Returns:
            list[list[int]]: list of list of nodes at each level
        """
        if self.root is None:
            return []
        
        Q: deque['BSTNode'] = deque([self.root])
        result: list[list[int]] = []
         
        while len(Q) != 0:
            level_size: int = len(Q)
            level_nodes: list[int] = []
            
            for _ in range(level_size):
                curr_parent: BSTNode = Q.popleft() # top element of the queue
                level_nodes.append(curr_parent.value)
                
                if curr_parent.left is not None:
                    Q.append(curr_parent.left)
                if curr_parent.right is not None:
                    Q.append(curr_parent.right)
            result.append(level_nodes)
        
        return result
            
            
            
        
            
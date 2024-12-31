from dataclasses import dataclass, field
from typing import Optional

@dataclass
class BSTNode:
    value: int
    right: Optional['BSTNode'] = field(default=None)
    left: Optional['BSTNode'] = field(default=None)


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[BSTNode] = None

    def insert(self, val: int) -> None:
        pass

    def search(self, val: int) -> Optional[BSTNode]:
        pass

    def delete(self, val: int) -> None:
        pass

    def inorder_traversal(self) -> list[int]:
        return []

    def preorder_traversal(self) -> list[int]:
        return []

    def postorder_traversal(self) -> list[int]:
        return []

    def find_min(self) -> Optional[int]:
        pass

    def find_max(self) -> Optional[int]:
        pass

    def is_empty(self) -> bool:
        return False
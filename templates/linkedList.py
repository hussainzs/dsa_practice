from typing import Any, Optional

class Node:
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
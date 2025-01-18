from collections import deque, defaultdict

def dfs_traversal(graph: dict[int, list[int]], start: int = 0) -> list[int]:
    """Performs Depth-First Search traversal of the graph.
    Will only return the connected component of the starting node. If graph is disconnected, won't return the entire graph.
    
    Args:
        graph (dict[int, list[int]]): Graph represented as adjacency list
        start (int, optional): Starting node. Defaults to 0.
    
    Returns:
        list[int]: Nodes in DFS traversal order
        
    Example:
        >>> graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        >>> dfs_traversal(graph, 0)
        [0, 1, 3, 2]
    
    Time: O(V + E) where V is vertices and E is edges
    Space: O(V) for stack and visited set
    """
    stack: deque[int] = deque([start])
    visited: set[int] = {start}
    result: list[int] = []
    
    while stack:
        current_node: int = stack.pop()
        result.append(current_node)
        
        for neighbor in reversed(graph[current_node]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                
    return result

    
def dfs_trees(graph: dict[int, list[int]]) -> list[list[int]]:
    """Returns DFS trees (forest) for the graph, handling disconnected components.
    Uses iterative approach to prevent stack overflow.

    Args:
        graph (dict[int, list[int]]): Graph represented as adjacency list

    Returns:
        list[list[int]]: List of DFS trees where each tree is a list of nodes
            in DFS traversal order

    Example:
        >>> graph = {0: [1], 1: [0], 2: [3], 3: [2]}
        >>> dfs_trees(graph)
        [[0, 1], [2, 3]]

    Time: O(V + E) where V is vertices and E is edges
    Space: O(V) for stack and visited set
    """
    n: int = len(graph)
    global_visited: set[int] = set()
    result: list[list[int]] = []
    
    for root in range(n):
        if root not in global_visited:
            stack: deque[int] = deque([root])
            global_visited.add(root)
            current_tree: list[int] = []
            
            while stack:
                current_node: int = stack.pop()
                current_tree.append(current_node)
                
                for neighbor in reversed(graph[current_node]):
                    if neighbor not in global_visited:
                        global_visited.add(neighbor)
                        stack.append(neighbor)
            
            # by this point we have traversed the entire connected component         
            result.append(current_tree)
    
    return result
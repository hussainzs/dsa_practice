from collections import deque

"""
graph = list[list[int]] adjacency list
i.e. = [[1,2,3], [5,6], ...]
"""

def breath_first_search(graph: list[list[int]], start: int) -> list[int]:
    """
    Perform a breadth-first search (BFS) on the graph starting from the given node.

    Args:
        graph (dict[int, list[int]]): A dictionary where the key represents the node and the value represents its neighbors.
        start (int): The starting node for the BFS.

    Returns:
        list[int]: A list of nodes in the order they were discovered during the BFS.
    """
    Q: deque[int] = deque([start])
    discovered: list[int] = []
    
    while len(Q) != 0:
        curr_parent: int = Q.popleft() # popLeft gets the node at the front of the queue
        discovered.append(curr_parent)
        for neighbor in (graph[curr_parent]):
            if neighbor not in discovered:
                Q.append(neighbor)
                
    return discovered
    
    
def depth_first_search(graph: list[list[int]]) -> list[list[int]]:
    """Returns a list of list where each inner list represents the dfs tree starting from a node. 
    If the input graph is disconnected there will be multiple trees thus multiple inner lists. 
    If graph is connected then there will be one inner list containing all of the nodes traversed in depth first fashion.

    Args:
        graph (list[list[int]]): list of list where the index of the inner list represents the node and content represents its neighbors. 

    Returns:
        list[list[int]]: dfs trees in list of list representation
    """
    stack: deque[int] = deque()
    global_visited: set[int] = set() 
    result: list[list[int]] = []
    
    for i in range(len(graph)): # we need this extra for loop beacuse graph maybe disconnected and we need to jump to vertices unreachable from others 
        if i not in global_visited:
            stack.append(i) # this will be root of this dfs tree
            current_tree: list[int] = [] # start a new tree 
            
            while len(stack) != 0:
                current_node: int = stack.pop()
                if current_node not in global_visited:
                    current_tree.append(current_node)
                    global_visited.add(current_node)
                    # Add unvisited neighbors only 
                    for neighbor in reversed(graph[current_node]):
                        if neighbor not in global_visited: # small optimizion for stack space by not adding unnecessary seen vertices
                            stack.append(neighbor)
                    
            result.append(current_tree) # add the tree we have built into result
    
    return result
    

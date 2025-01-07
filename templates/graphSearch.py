from collections import deque

"""
graph = list[list[int]] adjacency list
i.e. = [[1,2,3], [5,6], ...]
"""

def breadth_first_search(graph: list[list[int]], start: int) -> list[list[int]]:
    """
    Perform a breadth-first search (BFS) on the graph starting from the given node.

    Args:
        graph (List[List[int]]): Adjacency list representation of graph
        where graph[i] contains neighbors of vertex i

    Returns:
        list[list[int]]: A list of lists, where each inner list contains the values of the nodes 
            at a specific level of the tree. If the tree is empty, an empty list is returned.
    """
    Q: deque[int] = deque([start])
    discovered: set[int] = set([start])
    result: list[list[int]] = []
    
    while len(Q) != 0:
        level_size: int = len(Q)
        current_level: list[int] = []
        
        for _ in range(level_size): # keep popping the entire queue until we get all of this level
            curr_parent: int = Q.popleft() # popLeft gets the node at the front of the queue
            current_level.append(curr_parent)
            
            for neighbor in (graph[curr_parent]):
                if neighbor not in discovered:
                    Q.append(neighbor)
                    discovered.add(neighbor)
        result.append(current_level) # add the current level into the result
    
    return result
    
    
def depth_first_search(graph: list[list[int]]) -> list[list[int]]:
    """Returns a list of list where each inner list represents the dfs tree starting from a node. 
    If the input graph is disconnected there will be multiple trees thus multiple inner lists. 
    If graph is connected then there will be one inner list containing all of the nodes traversed in depth first fashion.

    Args:
        graph (List[List[int]]): Adjacency list representation of graph
        where graph[i] contains neighbors of vertex i
        
    Returns:
        List[List[int]]: List of DFS trees where each inner list represents
        vertices visited in DFS order starting from different components
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
    

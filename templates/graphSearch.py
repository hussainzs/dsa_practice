from collections import deque

"""
graph = list[list[int]] adjacency list
i.e. = [[1,2,3], [5,6], ...]
"""

def breath_first_search():
    pass
    
def depth_first_search(graph: list[list[int]]) -> list[list[int]]:
    """Returns a list of list where each inner list represents the dfs tree starting from a node. 
    If the input graph is disconnected there will be multiple trees thus multiple inner lists. 
    If graph is connected then there will be one inner list containing all of the nodes traversed in depth first fashion.

    Args:
        graph (list[list[int]]): list of list where the index of the inner list represents the node and content represents its neighbors

    Returns:
        list[list[int]]: dfs trees in list of list representation
    """
    stack: deque[int] = deque()
    visited: list[int] = []
    result: list[list[int]] = []
    
    for i in range(len(graph)):
        if i not in visited: # if this node is already seen then all of its children are also seen by the property of dfs
            stack.append(i)
        
            while len(stack) != 0:
                current_node: int = stack.pop() # pops from the right = Last Inserted element
                if current_node not in visited:
                    visited.append(current_node)
                    stack.extend(graph[current_node]) # insert children of current node
                    
            result.append(visited) # add the connected tree starting from "start" node into dfs
            visited = [] # reset visited
    
    return result
    

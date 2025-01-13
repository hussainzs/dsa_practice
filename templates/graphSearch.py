from collections import deque

"""
graph = list[list[int]] adjacency list
i.e. = [[1,2,3], [5,6], ...]
"""

def breadth_first_search(graph: list[list[int]], start: int) -> list[list[int]]:
    """
    Performs BFS on a graph and returns nodes organized by levels.

    Args:
        graph (List[List[int]]): Adjacency list representation of graph
        where graph[i] contains neighbors of vertex i
    
    Returns:
        List[List[int]]: A list of lists, where each inner list contains nodes 
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
    global_visited: set[int] = set()
    result: list[list[int]] = []
    
    for i in range(len(graph)):  # Handle disconnected components
        if i not in global_visited:
            stack: deque[int] = deque([i])  # Initialize with root of this new tree
            global_visited.add(i)
            current_tree: list[int] = []
            
            while len(stack) != 0:
                current_node: int = stack.pop()
                current_tree.append(current_node)  
                
                # Add unvisited neighbors
                for neighbor in reversed(graph[current_node]):
                    if neighbor not in global_visited:
                        stack.append(neighbor)
                        global_visited.add(neighbor)  # Mark as visited when adding to stack
            
            result.append(current_tree)
    
    return result


def calculate_indegree(edges_arr: list[tuple[int, int]]) -> list[int]:
    n = len(edges_arr)
    indegree: list[int] = [0 for _ in range(n)] # populate n zeros
    for src, dest in edges_arr:
        indegree[dest] += 1
    return indegree
    

# Naive Approach: O(v^2) find a source node O(n) this happens n times so O(n^2)
# Optimized Approach: O(V + E) 👇
'''
We maintain the indegree of each node (initially O(n) to find all in-degrees but to maintain O(1)). 
Each time we remove a node from the graph, we decrement the indegree of all of its outneighbors. 
If the indegree of any of these nodes becomes 0, then we add it to our list.
'''
def topological_sort(graph: list[list[int]]) -> list[int]:
    """
    Performs topological sort on a directed acyclic graph (DAG).

    Args:
        graph (List[List[int]]): Adjacency list representation of graph
        where graph[i] contains neighbors of vertex i

    Returns:
        List[int]: A list of vertices in topologically sorted order.
    """
    return []

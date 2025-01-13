from collections import deque
from collections import defaultdict

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


def convert_edgeList_to_adjList(edgeList: list[tuple[int, int]]) -> dict[int, list[int]]:
    """Convert any edge list represnetation to adjList in O(E) time

    Args:
        edgeList (list[tuple[int, int]]): edge list for example: [(0, 1), (1, 2), (1, 3), (3, 2), (3, 4)]

    Returns:
        dict[int, list[int]]: adjacency representation for example: {0: [1], 1: [2, 3], 2: [], 3: [2, 4], 4: []}
    """
    # Initialize an adjacency list using defaultdict, which will automatically create an empty list for any new key
    adjList: defaultdict[int, list[int]] = defaultdict(list)
    
    for src, dest in edgeList:
        # Append the destination node to the list of neighbors for the source node
        # If the source node does not exist in the adjacency list, defaultdict will create a new list for it and then append dest to it
        adjList[src].append(dest)
        
    return adjList
    

def calculate_indegree_from_edgeList(edge_list: list[tuple[int, int]]) -> list[int]:
    """
    You are given a graph with n nodes, where each node has an integer value from 0 to n - 1.
    The graph is represented by a list of edges, where edges[i] = [u, v] is a directed edge from node u to node v. 
    Write a function to calculate the indegree of each node in the graph.

    Example
    Input: edges = [(0, 1), (1, 2), (1, 3), (3, 2), (3, 4)] where n = 5
    Output: [0, 1, 2, 1, 1]

    Args:
        edges_arr (list[tuple[int, int]]): list of edges

    Returns:
        list[int]: indegree if each node
    """
    n: int = max(max(u, v) for u, v in edge_list) + 1 # O(E) + O(E) = O(E) 
    indegree: list[int] = [0 for _ in range(n)] # populate n zeros
    for src, dest in edge_list:
        indegree[dest] += 1
    return indegree
    

def calculate_indegree_from_adjList(adj_list: dict[int, list[int]]) -> list[int]:
    """ Calculate indegree of each node in adj list
    Input: adj_list = {0: [1], 1: [2, 3], 2: [], 3: [2, 4], 4: []}
    Output: [0, 1, 2, 1, 1]

    Args:
        adj_list (dict[int, list[int]]): adjacency list representation of the graph

    Returns:
        list[int]: indegree of each list
    """
    indegree: list[int] = [0 for _ in range(len(adj_list))]
    for values in adj_list.values():
        for v in values:
            indegree[v] += 1
    return indegree

# Naive Approach: O(v^2) find a source node O(n) this happens n times so O(n^2)
# Optimized Approach: O(V + E) 👇
'''
We maintain the indegree of each node (initially O(n) to find all in-degrees but to maintain O(1)). 
Each time we remove a node from the graph, we decrement the indegree of all of its outneighbors. 
If the indegree of any of these nodes becomes 0, then we add it to our list.
'''
def topological_sort(graph: dict[int, list[int]] | list[tuple[int, int]]) -> list[int]:
    """Finding topological ordering of the given graph.
    Input examples:
    adj_list =  {0: [1], 1: [2, 3], 2: [], 3: [2, 4], 4: []}
    edge list =  [(0, 1), (1, 2), (1, 3), (3, 2), (3, 4)]

    Args:
        graph (dict[int, list[int]] | list[tuple[int, int]]): either adjacency list or edge list

    Returns:
        list[int]: topological ordering - dependency perserving ordering of the vertices
    """
    
    # The algorithm goes like this kahns toposort 
    '''
    1. Calculate the indegree of each node.
    2. Add all nodes with an indegree of 0 to a queue.
    3. While the queue is not empty:
        4. Dequeue the first node from the queue and add it to the topological order.
        5. For each neighbor of the node, decrement its indegree by 1. If the neighbor's indegree is now 0, add it to the queue.
    Return the topological order.
    '''
    # claulcate indegree of each node
    indegree: list[int] = []
    if isinstance(graph, dict): # if we get adjacency list
        indegree = calculate_indegree_from_adjList(graph)
    elif isinstance(graph, list): # if we get edge list
        indegree = calculate_indegree_from_edgeList(graph)
    else:
        raise TypeError("Input is not of the desired type")
        
    # add all indegree 0 to queue
    Q: deque[int] = deque([])
    for index, degree in enumerate(indegree):
        if degree == 0:
            Q.append(index)
    

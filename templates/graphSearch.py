from collections import deque
from collections import defaultdict

"""
graph = adjacency list: dict[int, list[int]]
{0: [1], 1: [2, 3], 2: [], 3: [2, 4], 4: []}
"""

def bfs_traversal(graph: dict[int, list[int]], start: int) -> list[int]:
    """Returns List of nodes traversed in BFS fashion. 

    Args:
        graph (dict[int, list[int]]): undirected graph represented as adjacency list
        start (int): start node

    Returns:
        list[int]: Nodes traversed in BFS fashion.
    
    Time Complexity: O(V + E) where V is number of vertices and E is number of edges
    Space Complexity: O(V) for queue and visited set
    """
    Q: deque[int] = deque([start])
    visited: set[int] = {start}
    result: list[int] = []
    
    while Q: # until Q is not empty
        current_node: int = Q.popleft() # pop the top in O(1)
        result.append(current_node) # Add to result when processing
        
        # go through all the neighbors and add them to queue as well
        neighbors: list[int] = graph[current_node]
        for neighbor in neighbors:
            # add only if we havent already visited otherwise we maybe be stuck in a loop
            if neighbor not in visited:
                visited.add(neighbor) # Mark visited when adding to queue
                Q.append(neighbor)
                
    return result

def bfs_levels(graph: dict[int, list[int]], start: int = 0) -> list[list[int]]:
    """Performs level-order traversal of graph, grouping nodes by their distance from start.
    
    A level consists of all nodes that are the same distance from the start node.
    Level 0 contains the start node, level 1 contains its immediate neighbors,
    level 2 contains nodes that are two edges away, and so on.

    Args:
        graph (dict[int, list[int]]): Graph represented as adjacency list where
            key is node and value is list of its neighbors
        start (int, optional): Starting node for traversal. Defaults to 0.

    Returns:
        list[list[int]]: List of levels, where each level is a list of nodes
            at the same distance from start node.

    Example:
        >>> graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
        >>> bfs_levels(graph, 0)
        [[0], [1, 2], [3]]

    Time Complexity: O(V + E) where V is number of vertices and E is number of edges
    Space Complexity: O(V) for queue and visited set
    """
    Q: deque[int] = deque([start])
    discovered: set[int] = {start}
    result: list[list[int]] = []
    
    while Q:
        # at this point whatever is in the Queue belongs to one level
        level_size: int = len(Q)
        current_level: list[int] = []
        
        # we will pop all the current elements in the Queue. This means all the remaining elements will be next level
        for _ in range(level_size):
            current_node: int = Q.popleft()
            current_level.append(current_node)
            
            for neighbor in graph[current_node]:
                if neighbor not in discovered:
                    discovered.add(neighbor)
                    Q.append(neighbor)
                    
        result.append(current_level)
    
    return result
            
        
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
    topoOrder: list[int] = []
    
    # if input is edgelist convert to adjacency list
    if isinstance(graph, list):
        graph = convert_edgeList_to_adjList(graph)
    
    # find the indegree
    indegree: list[int] = calculate_indegree_from_adjList(graph)
        
    # add all indegree 0 to queue
    Q: deque[int] = deque([])
    for index, degree in enumerate(indegree):
        if degree == 0:
            Q.append(index) # here index is the node
    
    while Q: # until Q is not empty
        # deque first node and add it to topo order
        sourceNode: int = Q.popleft()
        topoOrder.append(sourceNode)
        
        # for each neighbor of this node decrement indegree by 1
        for neighbor in graph[sourceNode]:
            indegree[neighbor] -= 1
            if indegree == 0:
                # if indegree has become 1 then add to Queue
                Q.append(neighbor)
    
    return topoOrder
        
        
        
        
from collections import deque
from collections import defaultdict

"""
graph = adjacency list: dict[int, list[int]]
{0: [1], 1: [2, 3], 2: [], 3: [2, 4], 4: []}
"""

def breadth_first_search(graph: dict[int, list[int]], start: int) -> list[int]:
    """Returns List of nodes traversed in BFS fashion. 

    Args:
        graph (dict[int, list[int]]): undirected graph represented as adjacency list
        start (int): start node

    Returns:
        list[int]: Nodes traversed in BFS fashion.
    """

    
    
def depth_first_search(graph: dict[int, list[int]]) -> list[list[int]]:
    """Uses an Iterative approach to save stack space. 
    Returns a list of list where each inner list represents the dfs tree.

    Args:
        graph (dict[int, list[int]]): undirected graph represented as adjacency list

    Returns:
        list[list[int]]: a list of list where each inner list represents the dfs tree.
        each node is traversed in dfs fashion
    """


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
        
        
        
        
from collections import deque

def bfs_traversal(graph: dict[int, list[int]], 
                  start: int) -> list[int]:
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

def bfs_levels(graph: dict[int, list[int]], 
               start: int = 0) -> list[list[int]]:
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

def bfs_shortest_distance_on_grid(grid: list[list[int]], 
                                  start: tuple[int, int],
                                  end: tuple[int, int]) -> int:
    """Finds the shortest path between start and end coordinate.

    Args:
        grid (list[list[int]]): A grid with 0 for valid cell and 1 for blocked cell.
        start (tuple[int, int]): starting (x,y) coodinate for example 0,0
        end (tuple[int, int]): ending (x,y) coordinate for example r-1, c-1 where r = num of rows and c = num of columns

    Returns:
        int: shortest path between the start and end. -1 if no path exists from start to end
    
    Example:
        >>> grid = [[0, 1, 0],
                    [0, 0, 1],
                    [1, 0, 0]]
        start = (0,0)
        end = (2, 2)
        answer = 4

    Time Complexity: O(r * c) where r is number of rows and c number of columns
    Space Complexity: O(r * c) 
    """
    numRows: int = len(grid)
    numCols: int = len(grid[0])
    
    def is_valid_coordinate(coordinate: tuple[int, int]) -> bool:
        """Method to check if a coordinate is valid"""
        x, y = coordinate
        return 0 <= x < numRows and 0 <= y < numCols and grid[x][y] == 0
    
    # edge case if start or end are invalid coordinate
    if not is_valid_coordinate(start) or not is_valid_coordinate(end):
        return -1
    
    # edge case start and end are same 
    if start == end: # == checks for value equality so thats good here
        return 0
    
    # otherwise lets begin
    # define the valid movements up, down, left, right
    # Note that [-1,0] represent dx = -1 and dy = 0 which means we go up a row in same column. This represents UP
    # [1,0] = DOWN, [0,-1] = LEFT, [0,1] = RIGHT
    movements: list[list[int]] = [[-1,0], [1,0], [0,-1], [0,1]]
    
    # create a r * c array initialize with 0 for distance and False for visited
    dist: list[list[int]] = [[0] * numCols for _ in range(numRows)] 
    visited: list[list[bool]] = [[False] * numCols for _ in range(numRows)]
    
    # initialize Q
    Q: deque[tuple[int, int]] = deque()
    
    # add the starting point into Q
    Q.append(start)
    visited[start[0]][start[1]] = True
    
    # run bfs until Q is empty
    while len(Q):
        curr_x, curr_y = Q.popleft() # pop the top
        
        # try going up, down, left, right
        for dx, dy in movements:
            new_x: int = curr_x + dx
            new_y: int = curr_y + dy
            
            # if this cell is in bounds and not already visited
            # note we must first check if the new coordinates are valid before checking visited otherwise it may throw index error
            if is_valid_coordinate((new_x, new_y)) and visited[new_x][new_y] == False:
                Q.append((new_x, new_y)) # append to queue
                visited[new_x][new_y] = True # mark it as visited 
                dist[new_x][new_y] = dist[curr_x][curr_y] + 1 # this new cell took 1 more step so add 1 to distance
                
                # if we reached the end coordinate then we are done so terminate early
                if new_x == end[0] and new_y == end[1]:
                    return dist[new_x][new_y]
    
    # return -1 if we havent reached the end (it can only be zero if we haven't reached it, we already resolved the edge case where start == end for dist = 0)
    if dist[end[0]][end[1]] == 0:
        return -1
    else:
        return dist[end[0]][end[1]]
        
        
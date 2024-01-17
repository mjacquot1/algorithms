import collections

def is_connected_union_join(n, edges, start, target):
    ''' Given a list of edges, a start, and a target
        return true if you can reach the target from start'''
    # This is doable if start & target are in the same union

    # This will state what node is above it
    #   in the heierarchy
    parent = list(range(n))

    # Rank is how many children the node has
    rank = [1] * n

    def find_head(node):
        head = node

    
        # While the node is not the parent of itself
        while head != parent[head]:
            # Once we have walke the whole chain
            # We will reach it's head node
            head = parent[head]

        return head

    def union(n_1, n_2):
        # Find the head nodes for each
        h_1, h_2 = find_head(n_1), find_head(n_2)

        # We know that the nodes are connected.
        # Link l_2 to l_2
        if rank[h_1] == rank[h_2]:
            parent[h_2] = h_1
            rank[h_1] += rank[h_2]
        
        # If the head of node one has less children
        #   than node two, then connected node one
        #   to node 2 as a child
        elif rank[h_1] < rank[h_2]:
            parent[h_1] = h_2
            rank[h_2] += rank[h_1]


        # else, connect node two to node one
        #   as a child
        elif rank[h_1] > rank[h_2]:
            parent[h_2] = h_1
            rank[h_1] += rank[h_2]

    # unionize all edges
    for n_1, n_2 in edges:
        union(n_1, n_2)

    # see if start and target have the same head
    return find_head(start) == find_head(target)

def count_components_union_join(n, edges):
    ''' Given n nodes, and a list of connecting edges
        count how many individual unconnected graphs there are. '''

    # This will state what nde is above it
    #   in the heierarchy
    parent = list(range(n))

    # Rank is how many children the node has
    rank = [1] * n

    def find_head(node):
        head = node

        # While the node is not the parent of itself
        while head != parent[head]:
            # While we go up the chain,
            #   if we know a node has a parent 2 levels above it
            #   replace it's parent with it's granparent
            grandparent = parent[parent[head]]
            parent[head] = grandparent

            # Once we have walke the whole chain
            # We will reach it's head node
            head = parent[head]

        # Return the head node
        return head

    def union(n_1, n_2):
        # Find the head nodes for each
        h_1, h_2 = find_head(n_1), find_head(n_2)

        # The nodes are already joined
        #   along the same chain
        if h_1 == h_2:
            return 0

        # We know that the nodes are connected.
        # If the head of node one has less children
        #   than node two, then connected node one
        #   to node 2 as a child
        if rank[h_1] < rank[h_2]:
            parent[h_1] = h_2
            rank[h_2] += rank[h_1]

        # else, connect node two to node one
        #   as a child
        else:
            parent[h_2] = h_1
            rank[h_1] += rank[h_2]

        return 1

    # Result is many node there are
    res = n

    # minus how many get combined based on edges
    for n_1, n_2 in edges:
        res -= union(n_1, n_2)

    return res

def is_connected_undirected_dfs(edges, start, target):
    ''' Given a list of edges, a start, and a target
        return true if you can reach the target from start'''

    # Create a stack to track what nodes to visit
    stack = [start]

    # Since theres risk of a loop.
    # Keep track of nodes visited.
    visited = set()

    # Make an adjacency list.
    # Remember, each node needs a spot
    #   in the hash.
    def make_adj_list(edges):
        adj_list = collections.defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        return adj_list
    
    
    adj_list = make_adj_list(edges)

    # While there are still more nodes to traverse
    while stack:
        curr_node = stack.pop()

        # If you've seen this node before, skip
        if curr_node in visited:
            continue

        # If the node is the taret, return True
        if curr_node == target:
            return True

        # Add processed node to visited
        visited.add(curr_node)

        # Add all connected nodes to the stack
        stack = stack + [ x for x in adj_list[curr_node] ]

    return False

def count_components_undirected_dfs(n, edges):
        
    # Make an adjacency list.
    # Remember, each node needs a spot
    #   in the hash.
    def make_adj_list(edges):
        adj_list = collections.defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        return adj_list
    

    # Make sure to visit every connected node
    def traverse_nodes(node, adj_list, visited):
        # If given node is already visited
        #   don't count it
        if node in visited:
            return 0
        
        # Create a stack to track what nodes to visit
        stack = [node]

        # While there are still more nodes to traverse
        while stack:
            curr_node = stack.pop()

            # If you've seen this node before, skip
            if curr_node in visited:
                continue
            
            # Add processed node to visited
            visited.add(curr_node)

            # Add all connected nodes to the stack
            stack = stack + adj_list[curr_node]
        
        # Once all connected nodes are explored
        #   return 1 to count it all as a
        #   single connected component
        return 1
    


    # Since theres risk of a loop.
    # Keep track of nodes visited.
    visited = set()

    adj_list = make_adj_list(edges)

    count = 0

    # go through each node
    for i in range(n):
        # Add to the count if
        #   it is a new connected component
        count += traverse_nodes(i, adj_list, visited)

    return count

def number_of_islands(matrix, water=0, land=1):
    if not matrix:
            return

    def str_coord(row, col):
        return f'{row}:{col}'

    def is_valid(matrix, visited, row, col, invalid="0"):
        r_low, r_high = -1, len(matrix)
        col_low, col_high = -1, len(matrix[0])

        if ( r_low < row < r_high
            and col_low < col < col_high
            and str_coord(row, col) not in visited 
            and matrix[row][col] != invalid):
            return True
        
        return False

    def bfs(matrix, row, col, visited, dirs):

        q = collections.deque([(row, col)])

        while q:
            row, col = q.popleft()

            if not is_valid(matrix, visited, row, col):
                continue
            
            visited.add(str_coord(row, col))
            for r_ch, c_ch in dirs:
                q.append((row+r_ch, col+c_ch))
        
        return 1
    
    dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
    
    islands = 0
    visited = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if is_valid(matrix, visited, row, col):
                islands += bfs(matrix, row, col, visited, dirs)
            else:
                visited.add(str_coord(row, col))

    return islands

def sentence_similarity(sen_1, sen_2, edges):
    if len(sen_1) != len(sen_2):
        print('wrong len')
        return False

    # create adj list
    def create_adj_list(edges):
        adj_list = collections.defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        return adj_list

    # run dfs to find path for each word pair
    def dfs_find(adj_list, start, target):

        if start == target:
            return True
        
        visited = set()
        
        stack = [start]

        while stack:
            curr_node = stack.pop()

            if curr_node in visited:
                continue

            if curr_node == target:
                return True

            visited.add(curr_node)
            stack = stack + adj_list[curr_node]

        return False

    adj_list = create_adj_list(edges)

    for w_1, w_2 in zip(sen_1, sen_2):
        if not dfs_find(adj_list, w_1, w_2):
            return False

    return True

def is_toeplitz_matrix(matrix):
    for row, arr in enumerate(matrix[1:], start=1):
        for i, val in enumerate(arr[1:], start=1):
            if val != matrix[row-1][i-1]:
                return False

    return True

def print_diagonals_from_row(matrix, row, col, left_right=True):
    inc = 1 if left_right else -1

    temp_arr = []
    while (-1 < row < len(matrix) 
            and -1 < col < len(matrix[row])):
        temp_arr.append(matrix[row][col])

        row += 1
        col += inc
    
    return temp_arr

def island_perimeter_greedy(matrix, water=0, land=1):
    def is_water(matrix, row, col, water=0):
        if (row >= len(matrix) or col >= len(matrix[0])
                or row < 0 or col < 0
                or matrix[row][col] == water):
            return True
        
        return False

    def is_coast(matrix, row, col, land=1):

        if matrix[row][col] != land:
            return 0

        perimeter = 0
        for r_inc, c_inc in ((-1,0), (1,0), (0,1), (0, -1)):
            if is_water(matrix, row+r_inc, col+c_inc):
                perimeter += 1
        
        return perimeter

    perimeter = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            perimeter += is_coast(matrix, row, col)

    return perimeter

def tick_tack_toe_winner(moves, n):

    def input_move(rows, cols, row, col, inc, winning=3):
        n = len(rows)

        rows[row] += inc
        cols[col] += inc

        if row == col:
            diag[0] += inc

        if row+col == n-1:
            diag[1] += inc

        if any(abs(x) == winning 
                for x in 
                (rows[row], cols[col], diag[0], diag[1])):
            return True
        
        return False

    rows, cols = [0]*n, [0]*n
    diag = [0]*2
    move_count = 0

    inc = 1

    for row, col in moves:
        if input_move(rows, cols, row, col, inc):
            return 'A' if inc == 1 else 'B'

        inc *= -1

    if move_count % n*n == 0:
        return 'Draw'
    else:
        return 'Pending'
    

class TicTacToe:
    def __init__(self, n: int):
        self.n = n

        self.rows, self.cols = [0]*n, [0]*n
        self.diag = [0,0]
        self.move_count = 0
        self.game_state = 0
        self.pending = 0
        self.curr_player = None


    def process_move(self, row, col):

        inc = 1 if self.move_count%2 == 0 else -1

        self.rows[row] += inc
        self.cols[col] += inc

        if row == col:
            self.diag[0] += inc
        
        if row+col == self.n-1:
            self.diag[1] += inc

        self.move_count += 1

    def is_winning(self, row, col):
        return any([abs(x) == self.n
                    for x in
                    (self.rows[row], self.cols[col], 
                    self.diag[0], self.diag[1])])

    def set_game_state(self, row, col):
        self.game_state = self.curr_player if self.is_winning(row, col) else self.pending

    def move(self, row: int, col: int, player: int) -> int:
        # Check that the move is valid 
        # Process move
        # See if move is a winning move
        # Return winner, Draw, or pending

        self.curr_player = player

        self.process_move(row, col)
        self.set_game_state(row, col)

        return self.game_state
    
def shortest_path_binary_matrix(matrix):
    def is_Valid(matrix, row, col, visited):
            return all((-1 < row < len(matrix),
                    -1 < col < len(matrix[0]),
                    (row, col) not in visited))


    def bfs(matrix, row, col, visited, path=0, obstacle=1):

        directions = (
            (1,0),
            (-1,0),
            (0,1),
            (0,-1),
            (1,1),
            (-1,1),
            (1,-1),
            (-1,-1),
        )

        q = collections.deque([(row, col, 1)])

        while q:
            row, col, distance = q.popleft()

            if not is_Valid(matrix, row, col, visited):
                continue
            
            if matrix[row][col] == obstacle:
                continue

            for r_adj, c_adj in directions:
                q.append((row+r_adj, col+c_adj, distance+1))

            visited[(row, col)] = distance

    visited = {}
    bfs(matrix, 0, 0, visited)

    if (len(matrix)-1, len(matrix[0])-1) in visited:
        return visited[(len(matrix)-1, len(matrix[0])-1)]
    else:
        return -1

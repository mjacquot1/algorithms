import collections

def is_connected_union_join(n, edges, start, target):
    ''' Given a list of edges, a start, and a target
        return true if you can reach the target from start'''
    # This is doable if start & target are in the same union

    # This will state what nde is above it
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

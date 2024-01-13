from collections import deque

from tests import simple_test_tree_root, complex_test_tree_root, edge_cases, test_delete, test_tree_sum

def compare_trees_recursive(p, q):

    # Base Cases
    # 1. p & q are null
    # 2. p is null, q is not null
    # 3. p is not null, q is null
    # 4. Neither is null, values dont match
    
    # 1
    if not p and not q:
        return True
    # 2 & 3
    if not p or not q:
        return False
    # 4
    if p.val != q.val:
        return False
    
    # Return comparing the left and the right branches
    # At some point, they should all hit a None 
    return (compare_trees(p.left, q.left) 
            and compare_trees(p.right, q.right))

def compare_trees_iterative(p, q):
    p_stack = [p]
    q_stack = [q]

    while p_stack and q_stack:
        curr_p = p_stack.pop()
        curr_q = q_stack.pop()

        # Base Cases
        # 1. p & q are null
        # 2. p is null, q is not null
        # 3. p is not null, q is null
        # 4. Values don’t match

        # 1 & 4
        # Checks that neither curr_p
        # nor curr_q is None
        # Also checks curr_p.val == curr_q.val
        if (curr_p and curr_q
            and curr_p.val == curr_q.val):

            p_stack.append(curr_p.left)
            q_stack.append(curr_q.left)

            p_stack.append(curr_p.right)
            q_stack.append(curr_q.right)
        
        # 2 & 3
        # At this point:
        # if curr_p or curr_q: 
        # one has value and the other is None
        # or curr_p != curr_q
        elif curr_p or curr_q:
            return False

def find_target_in_bst(root, target):
    ''' O(h) complexity, h == height '''

    # curr_node = root to start        
    curr_node = root

    # This ends if curr_node is none
    # like we hit a dead end
    while curr_node:
        if target == curr_node.val:
            return curr_node
        
        # If target <= curr_node.val
        # Move down the left
        elif target <= curr_node.val:
            curr_node = curr_node.left

        # If target > curr_node.val
        # Move down the right
        elif target > curr_node.val:
            curr_node = curr_node.right

    # Return None if no node is found
    return None

def bst_insert(root, val):
    
    curr_node = root
    
    # Keep going until you hit a blank node
    while curr_node:
        # If target <= curr_node.val
        # try going left.
        # If left == None, insert new node
        if val <= curr_node.val:
            if curr_node.left:
                curr_node = curr_node.left
            else:
                curr_node.left = Node(val)
                curr_node = None
        
        # If target > curr_node.val
        # try going right.
        # If right == None, insert new node
        elif val > curr_node.val:
            if curr_node.right:
                curr_node = curr_node.right
            else:
                curr_node.right = Node(val)
                curr_node = None

def in_order_traversal_recursive(root):
    
    # Base cases
    # node is None
    if not root:
        return
    
    # Work all the way down left
    in_order_traversal_recursive(root.left)
    
    # If Done, print root.val
    print(root.val)
    
    # Then work down the right
    in_order_traversal_recursive(root.right)

def in_order_traversal_iterative(root):
    
    stack = []
    ret_arr = []
    
    # Set the current node to root
    curr_node = root
    
    
    while True:
        # Check curr_node != None
        # If not, and it to stack
        # to keep track of whats visited.
        # Then keep trying to go left.
        if curr_node: 
            stack.append(curr_node)
            curr_node = curr_node.left
        
        # If there's no more to the left
        # Return to prev on stack
        # and go to the right once
        elif stack:
            curr_node = stack.pop()
            
            # Add curr_nodeto ret_arr here.
            # This is the farthest left
            # on the branch
            ret_arr.append(curr_node.val)
            curr_node = curr_node.right
            
        # If we've exhausted the stack
        # break
        else:
            break
        
    return ret_arr

def pre_order_traversal_iterative(root):

    stack = []
    ret_arr = []
    
    # Set the current node to root
    curr_node = root
    
    
    while True:
        # Check curr_node != None
        # If not, and it to stack
        # to keep track of whats visited.
        # Then keep trying to go left.
        if curr_node: 
            stack.append(curr_node)
            
            # Add curr_node to ret_arr here.
            # This is the right node 
            # on the branch
            ret_arr.append(curr_node.val)
            
            curr_node = curr_node.left
        
        # If there's no more to the left
        # Return to prev on stack
        # and go to the right once
        elif stack:
            curr_node = stack.pop()
            curr_node = curr_node.right
            
        # If we've exhausted the stack
        # break
        else:
            break
        
    return ret_arr

def post_order_traversal(root, ret_arr):
    
    # Base Cases
    # root is None
    if not root:
        return
    
    # Work all the way down left
    post_order_traversal(root.left, ret_arr)
    
    # Then work down the right
    post_order_traversal(root.right, ret_arr)
    
    # Add root.val to ret_arr here
    # This is the first time This
    # Node is seen
    ret_arr.append(root.val)


def breadth_first_traversal(root):
    ''' Tree Level Order Traversal '''
    
    # First make sure root != None
    if root == None:
        return []
    
    # Make a queue
    q = deque([root])
    ret_stack = []
    
    while q:
        # Get nodes in the order
        # they are found
        curr_node = q.popleft()
        ret_stack.append(curr_node.val)
        
        # Add nodes to the queue.
        # Usually left first.
        if curr_node.left:
            q.append(curr_node.left)
        if curr_node.right:
            q.append(curr_node.right)
        
    return ret_stack

def turn_tree_to_doubly_linked_list_iterate(root):
    if not root:
        return

    stack = []

    # Keep track of the first node found (left-most)
    # and the last node encountered
    first_vis, last_vis = None, None

    curr_node = root
    while True:
        if curr_node:
            # Used to find left-most nodes
            stack.append(curr_node)
            curr_node = curr_node.left

        elif stack:
            curr_node = stack.pop()

            if curr_node:
                # Now that we have a node 
                # that we know exists In-order
                # If a node has been visited already
                # It's the previous In-order
                if last_vis:
                    # Substitute "next" with "right"
                    last_vis.right = curr_node

                    #Subsitute "previous" with left
                    curr_node.left = last_vis
                
                # Else, this is the first node visited
                else:
                    first_vis = curr_node
                
                # Set this node to the last-visited
                last_vis = curr_node

            curr_node = curr_node.right

        else:
            break

    first_vis.left, last_vis.right = last_vis, first_vis
    return first_vis

                
def path_to_target_recurse(curr_node, target, path, ret_path):  
    ''' Find route from root to target'''
    # Base case
    # 1. Node is none
    # 2. Node is target

    if not curr_node:
        return
    
    # Append the current node to the path
    path.append(curr_node.val)

    # Make a deep copy of path to ret_path
    # if curr_node.val == target
    if curr_node.val == target:
        for i in path:
            ret_path.append(i)
    
    # Go left then right
    path_to_target_recurse(curr_node.left, target, path, ret_path)
    path_to_target_recurse(curr_node.right, target, path, ret_path)
    
    # If the target isn't on the left or right branches
    # pop this node from the path
    path.pop()


def delete_node_iterate(root, target, *args):

    def find_replacement_node(root):
        ''' go left, then farthest right '''
        
        parent_node = root
        curr_node = parent_node.left

        # Cases:
        # Node is leaf
        # Node has a left

        # If there are right nodes
        if curr_node.right:
            # Go as far right as you can
            # to find the biggest value
            # on this branch.
            while curr_node.right:
                # Keep track of cur_node's parent_node
                parent_node = curr_node
                curr_node = curr_node.right

            # If the found node has a left side
            # set the parent_node's right to equal
            # the found node's left
            # This could be simplified to just:
            #  parent_node.right = curr_node.left
            # since curr_node.left may be none anyways
            parent_node.right = curr_node.left

        # Elif there may still be a lef node. 
        # Set parent.left to it. If not, it will set to None
        else:
            parent_node.left = curr_node.left

        # Return highest val node on the branch
        return curr_node

    def point_parent(child_node, parent_node, rep_node):
        ''' Sets parent's left and right nodes if necessary '''

        # Deleted node is not the root, and has 
        # a parent node that needs to point to
        # new children, or no children anymore
        if parent_node:
            # child_node is on the left of parent
            if child_node.val <= parent_node.val:
                parent_node.left = rep_node

            # child_node is on the right of parent
            elif child_node.val > parent_node.val:
                parent_node.right = rep_node

    # Steps
    # 1. Find the node for deletion, keep track of it's parent
    # 2. Find the largest value node to the left of the deletion node,
    #       move that node out, point it's parent to it's left child
    # 3. Replace node with the largest-to-the-left node
    # 4. Swap pointers for the parent node to point to replacement
    # 5. If there's no parent, return the replacement node

    parent_node = None
    curr_node = root

    # First find the node and track the parent
    # If no node is found, it will return None.
    while curr_node:
        # if curr_node.val < target
        # Go to the right
        if curr_node.val < target:
            parent_node, curr_node \
            = curr_node, curr_node.right

        # if curr_node.val > target
        # Go to the left
        elif curr_node.val > target:
            parent_node, curr_node \
            = curr_node, curr_node.left
        
        # if curr_node.val == target
        # we found it!
        elif curr_node.val == target:
            break


    # If the target has been found
    if curr_node:
        
        # Cases:
        # Node has left & right
        # Node has neither
        # Node has a left or a right
        # Node is the root

        # If the node has a left and right child 
        if curr_node.left and curr_node.right:
            rep_node = find_replacement_node(curr_node)

            # Set the replacement nodes left & right
            # To point to deleted node's left & right
            rep_node.left, rep_node.right = \
                curr_node.left, curr_node.right

        else:
            # Now there is either no children
            # or one child.
            # Set rep_node to equal either one of the
            # children, or neither.
            rep_node = curr_node.left or curr_node.right

        # If there isn't a parent,
        # the replacement node is the new root
        if parent_node == None:
            root = rep_node
        
        # Run point_parent to point the parent node
        # to the proper replacement.
        # Whether that be another node, or none at all
        point_parent(curr_node, parent_node, rep_node)

        # Remove links that curr_node has
        # for garbage collection
        curr_node.left = curr_node.right = None

        return root

    return root

def delete_node_recursion(curr_node, target, parent_node=None):

    # First find deletion node
    # Find replacement node
    # Return root, new if necessary

    def go_farthest_right(curr_node, parent_node):
        
        # Base cases
        # 1. None passed in
        # 2. No node on the right
        # 3. Right-most node has no children
        # 4. Right-most node has left children
        if not curr_node.right:
            # If curr_node has a left child
            # parent_node.right will point to it
            # If no child, parent_node.right
            # Points to None
            parent_point(curr_node, parent_node)
            
            return curr_node.val
        
        
        return go_farthest_right(curr_node.right, curr_node)

    def parent_point(curr_node, parent_node):
        if parent_node:
                child = (curr_node.left or curr_node.right)
                if curr_node.val > parent_node.val:
                    parent_node.right = child 
                elif curr_node.val <= parent_node.val:
                    parent_node.left = child 

    # Base case
    # 1. Node is None
    # 2. Deletion node found

    if not curr_node:
        return
    
    if curr_node.val == target:
        ## Run deletion
        # If kids find largest value on left branch
        if curr_node.left and curr_node.right:
            curr_node.val = go_farthest_right(curr_node.left, curr_node)
            del curr_node 
        elif not parent_node:
            new_root = curr_node.left or curr_node.right
            del curr_node
            return new_root
        else:
            parent_point(curr_node, parent_node)

    return (delete_node_recursion(curr_node.left, target, curr_node)
            or delete_node_recursion(curr_node.right, target, curr_node))


def tree_sum_recursion(curr_node):

    # base case
    # If you hit None, return 0
    if not curr_node:
        return 0
    
    # val_sum is the sum of the left and right branches
    val_sum = (tree_sum_recursion(curr_node.left) \
               + tree_sum_recursion(curr_node.right))

    # Add on the curr_node val and return
    return val_sum + curr_node.val

def tree_sum_iterate(curr_node):
    if not curr_node:
        return 0
    
    stack = [curr_node]
    ret_sum = 0
    while stack:
        curr_node = stack.pop()
        ret_sum += curr_node.val 
        if curr_node.left:
            stack.append(curr_node.left)
        if curr_node.right:
            stack.append(curr_node.right)

    return ret_sum

def find_max_val_recursion(curr_node):
    
    # Base case
    # if you hit none, return
    if not curr_node:
        return
    
    return max(curr_node.val,
               (find_max_val_recursion(curr_node.left) or float('-inf')),
               (find_max_val_recursion(curr_node.right) or float('-inf')))

def find_max_val_iterate(curr_node):

    if not curr_node:
        return
    
    stack = [curr_node]
    ret_max = float('-inf')

    while stack:
        curr_node = stack.pop() 
        ret_max = max(curr_node.val, ret_max)
        if curr_node.left:
            stack.append(curr_node.left)
        if curr_node.right:
            stack.append(curr_node.right)

    return ret_max

def longest_root_to_leaf_recursive(curr_node, path, ret_path):
    
    # Base case
    # 1. If not curr_node, return None
    # 2. Leaf is found
    if not curr_node:
        return
    
    path.append(curr_node.val)

    if not curr_node.left and not curr_node.right:
        if len(path) > len(ret_path):
            ret_path.clear()
            for i in path:
                ret_path.append(i)
    
    longest_root_to_leaf_recursive(curr_node.left, path, ret_path)
    longest_root_to_leaf_recursive(curr_node.right, path, ret_path)
    path.pop()

def max_root_to_leaf_sum_recursion(curr_node, running_sum=0, max_sum = float('-inf')):

    # Base case
    # 1. If not curr_node
    # 2. Leaf is found
    if not curr_node:
        return float('-inf')
    
    running_sum += curr_node.val
    
    if not curr_node.left and not curr_node.right:
        return max(running_sum, max_sum)


    return max(max_root_to_leaf_sum_recursion(curr_node.left, 
                                            running_sum, max_sum),
                max_root_to_leaf_sum_recursion(curr_node.right, 
                                            running_sum, max_sum))

def lowest_common_ancestor_recursive(curr_node, 
                                     node_1, 
                                     node_2, 
                                     common_ancestor):

    # Base Cases:
    # 1. Not curr_node
    # 2. One is on left, other is on right
    # 3. Equals one, not found the other
    # 4. Equals one, found the other

    # 1
    if not curr_node:
        return False

    # Set 3 flags: A target node s on the left, on the right
    #   or is the current node

    # Set left & right to equal recursions
    # This will check to see if a target note is found on the left side
    left = lowest_common_ancestor_recursive(curr_node.left, 
                                            node_1, 
                                            node_2, 
                                            common_ancestor)

    # This will check to see if a target note is found on the right side
    right = lowest_common_ancestor_recursive(curr_node.right,
                                             node_1,
                                             node_2,
                                             common_ancestor)

    # This will check to see if the current node
    #   equals any of the target values
    found_node = (curr_node.val == node_1.val or curr_node.val == node_2.val)

    # Remember: True == 1, False == 0
    # If 2 flags are set, then both target nodes have been found
    if (found_node + left + right) >= 2:

        # Return the current node because these causes fave been met:
        # 1. Current node is a target, and the left side has a target
        # 2. Current node is a target, and the right side has a target
        # 3. Current node is not a target, but the left side has one
        # and so does the right side
        common_ancestor.append(curr_node)
        
    # If any flag is true, a target has been found. Return True.
    return found_node or left or right

def lowest_common_ancestor_iterate(curr_node, 
                                     node_1, 
                                     node_2):
    if not root:
        return

    # Flag to break when both nodes are found
    targets_found = False

    # Stack to traverse nodes
    # Each stack element: (node, parent, row #) 
    stack = [(root, None, 0)]

    # Hash to keep track of node & parent information  
    node_hash = {}

    while stack:
        # Get node from the top of the stack
        curr_node, parent_node, row_num = stack.pop()

        # Put that node in the hash, save it's parent and row number
        node_hash[curr_node] = {'parent':parent_node, 'row_num':row_num}

        # If both target nodes are now in the hash,
        # they have both been found. 
        # Set targets_found = True and stop looking.
        if node_1 in node_hash and node_2 in node_hash:
            targets_found = True
            break

        if curr_node.left:
            stack.append((curr_node.left, curr_node, row_num+1))
        if curr_node.right:
            stack.append((curr_node.right, curr_node, row_num+1))
    
    # If the tree has both target nodes in them
    if targets_found:
        # If node_1 is on a deeper tree level than node_2,
        # keep going up it's parents until its on the same level as node_2
        while node_hash[node_1]['row_num'] > node_hash[node_2]['row_num']:
            node_1 = node_hash[node_1]['parent']


        # If node_2 is on a deeper tree level than node_1,
        # keep going up it's parents until its on the same level as node_1
        while node_hash[node_2]['row_num'] > node_hash[node_1]['row_num']:
            node_2 = node_hash[node_2]['parent']

        # Now that we know both nodes are on the same tree level
        # Keep going up both their parents until they converge
        while node_1 != node_2:
            node_1 = node_hash[node_1]['parent']
            node_2 = node_hash[node_2]['parent']

        # Once the nodes have converged,
        # return either node.
        return node_1
    
    # If the tree does not have both target nodes in them,
    # their is no common ancestor.
    return None


if __name__ == '__main__':
    root = complex_test_tree_root()
    # print(in_order_traversal_iterative(root))
    # print(pre_order_traversal_iterative(root))
    # print(breadth_first_traversal(root))
    # root = delete_node_iterate(root, 7)
    # print(breadth_first_traversal(root))
    # path = []
    # path_to_target_iterate(root, 8, [], path)
    # print(path)
    # test_delete(delete_node_iterate,breadth_first_traversal)
    # test_delete(delete_node_recursion,breadth_first_traversal)
    # test_tree_sum(find_max_val_iterate, breadth_first_traversal)
    
    print(breadth_first_traversal(root))
    ret_path = []
    longest_root_to_leaf_recursive(root, [], ret_path)
    print(ret_path)
    print(max_root_to_leaf_sum_recursion(root))

    

from collections import deque

from tests import simple_test_tree_root, complex_test_tree_root

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
    in_order_traversal(root.left)
    
    # If Done, print root.val
    print(root.val)
    
    # Then work down the right
    in_order_traversal(root.right)

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

def delete_node(root, target):

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

        # Elif there are left nodes
        # Point parent_node left to them
        elif curr_node.left:
            parent_node.left = curr_node.left
        # Else, just get rid of the left node
        else:
            parent_node.left = None

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

    # Cases:
    # Node is a leaf
    # Node has a left
    # Node has a right
    # Node has both
    # Node is the root

    parent_node = None
    curr_node = root
    
    while curr_node:
        if curr_node.val == target:
            # If the node has a left and right child 
            if curr_node.left and curr_node.right:
                rep_node = find_replacement_node(curr_node)

                # Set the replacement nodes left & right
                # To point to deleted node's left & right
                rep_node.left, rep_node.right = \
                    curr_node.left, curr_node.right

            # elif the node is a leaf with no children
            elif not curr_node.left and not curr_node.right:
                # Set the replacement node to be none
                rep_node = None

            # elif the node only has a left child
            elif curr_node.left:
                # Set the replacement node to be to the left
                rep_node = curr_node.left

            # elif the child only has a right child
            elif curr_node.right:
                # Set the replacement node to be to the right
                rep_node = curr_node.right
            
            # Run point_parent to point the parent node
            # To the proper replacement
            # Whether that be another node, or none at all
            point_parent(curr_node, parent_node, rep_node)

            # Remove links that curr_node has
            curr_node.left = curr_node.right = None

            # If there isn't a parent,
            # the replacement node is the new root
            if parent_node == None:
                root = rep_node

            return root
                
        # Now that we're done checking curr_node
        # Set the parent node to curr_node
        parent_node = curr_node

        # if curr_node.val < target
        # Go to the right
        if curr_node.val < target:
            curr_node = curr_node.right

        # if curr_node.val > target
        # Go to the left
        elif curr_node.val > target:
            curr_node = curr_node.left

    return root



if __name__ == '__main__':
    root = complex_test_tree_root()
    print(in_order_traversal_iterative(root))
    print(pre_order_traversal_iterative(root))
    print(breadth_first_traversal(root))
    root = delete_node(root, 7)
    print(breadth_first_traversal(root))


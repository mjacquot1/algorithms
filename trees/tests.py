class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

def simple_test_tree_root():
    arr = [3,2,4,7,6,8]

    root = Node(5)
    for i in arr:
        bst_insert(root, i)

    return root

def complex_test_tree_root():
    arr = [5,15,2,7,12,20,0,4,6,9,11,14,18,25,1,3,8,13,16,19,23,17,21,24,22]

    root = Node(10)
    for i in arr:
        bst_insert(root, i)

    return root

def edge_cases():
    arrs = [
            [4,7,6,8,5,9,1],
            [2,1],
            [1,2],
            [1],
        ]

    # root = Node(10)
    # for arr in arrs:

    #     bst_insert(root, i)

    # return root

def test_delete(del_func, print_func, *args):
    tests = [
        ([4,7,6,8,5,9,1], 1),
        ([2,1], 1),
        ([1,2], 1),
        ([1], 1),
    ]

    while tests:
        arr, target = tests.pop()
        root = Node(arr[0])

        for i in arr[1:len(arr)]:
            
            bst_insert(root, i)

        print('---------------------------')
        print('Before: ', print_func(root))
        new_root = del_func(root, target)
        root = new_root #if new_root else root
        print('After:  ', print_func(root))

def test_tree_sum(sum_function, print_func, *args):
    tests = [
            [4,7,6,8,5,9,1],
            [2,1],
            [1,2],
            [1],
        ]
    
    while tests:
        arr = tests.pop()
        root = Node(arr[0])

        for i in arr[1:len(arr)]:
            bst_insert(root, i)

        print('Tree: ', print_func(root))
        print(sum_function(root, *args))
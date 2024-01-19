
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def merge_two_ordered_lists_new_list(self, l_1, l_2):
    # Create a node that you know will be at the
    #   Beginning of this list
    root = ListNode(float('-inf'))

    # Set curr_node to track what the furthest right
    #   node in the new list ist
    curr_node = root

    # Walk through both lists
    while l_1 and l_2:
        # If l_1.val <= l_2.val append it to the new list 
        if l_1.val <= l_2.val:
            curr_node.next = l_1
            l_1 = l_1.next

        # Else, append l_2 to the list
        else:
            curr_node.next = l_2
            l_2 = l_2.next

        # Move up in the new list
        curr_node = curr_node.next

    # Once one of the lists have been exhausted,
    #   then add what is left of the other list
    curr_node.next = (l_1 or l_2)

    # Move root up by one
    #   since we startet it with flaot('-inf')
    root = root.next

    return root

def reverse_linked_list(head):
    ''' Reverse a linked list in place '''

    # Set node to the head, and previous to None.
    # The reason for this, is that new_head will always be the head
    #   of the reversed list.
    node, new_head = head, None

    # Move node up the original list
    while node:
        # Make a temporary holder to the next
        #   node in the original list
        temp_node = node.next

        # The set node.next to the head of the new list
        #   and make it the new head
        node.next = new_head
        new_head = node

        # Then set the node to be 
        #   the next holder in the original list.
        node = temp_node

    # return the new head of the reversed list
    return new_head

def is_palindrome(head):
    stack = []
    node = head

    while node:
        stack.append(node.val)
        node = node.next

    return stack == stack[::-1]

def check_linked_list_cycle(head):
    ''' Tortoise and hare approach '''
    ''' Return true is theres an infinte cycle in list'''
    
    # If list is empy
    if not head:
        return False

    
    # Set up a slow point and fast pointer.
    # The slow pointer will move one node at a time.
    # The fast pointer will move two nodes at a time,
    #   and eventually either reach the end or loop back
    #   around to the slow pointer because it is slowly
    #   closing the distance between the two.
    s_p = head
    f_p = head.next

    while f_p != None and f_p != s_p:
        # Increment it up by one
        s_p = s_p.next

        # Increment by two, but check to make sure
        #   it hasn't hit the end of the list 
        f_p = f_p.next.next if f_p.next else None

    # If f_p is not none, its a a cycle
    return f_p != None
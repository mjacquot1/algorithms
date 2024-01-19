import collections
def custom_sort_string(s, order):
    # Make a count of how many times a char
    #   appears in the string
    string_count = collections.Counter(s)

    # Create a string to return
    ret_str = ''

    # Since the order string is in correct order
    #   walk through it, and append to ret_str
    for i in order:
        # Append each character by the amount of times
        #   they are seen in string s
        ret_str = ret_str + i*string_count[i]
        
        # Once done, remove it from the hash
        del string_count[i]

    # Then add all the leftovers in the hash
    for i in string_count: 
        ret_str = ret_str + i*string_count[i]

    return ret_str

def add_strings(s_1, s_2):
    if len(s_1) >= len(s_2):
        main, sec = s_1, s_2
    else:
        main, sec = s_2, s_1

    p_1, p_2 = len(main)-1, len(sec)-1

    ret_str = ''
    remainder = 0

    while p_1 >= 0:
        if p_2 >= 0:
            temp_sum = int(main[p_1]) + int(sec[p_2]) + remainder
            ret_str = str(temp_sum%10) + ret_str

            remainder = temp_sum//10
        else:
            temp_sum = int(main[p_1]) + remainder
            ret_str = str(temp_sum%10) + ret_str

            remainder = temp_sum//10

        p_1 -= 1
        p_2 -= 1

    if remainder:
        ret_str = str(remainder) + ret_str

    return ret_str

def valid_parenthesis(s):
    ''' Given a string s containing just the characters '(', ')', 
        '{', '}', '[' and ']', determine if the input string is valid.'''

    # Set up a hash of
    #   what a paranthesis would need
    #   too keep it closed.
    parens = {
        '}':'{',
        ']':'[',
        ')':'(',
    }

    # Make a stack to track
    #   open parenthesis that
    #   need to be closed.
    stack = []

    # iterate through each character in the string
    for i in s:
        # If this is a closing parenthesis
        #   it needs an open panrenthesis
        if i in parens:
            
            # If the stack is empty,
            #   theres no other parenthesis
            if not stack:
                return False

            # If the closing parenthesis equals
            #   its needed open, remove the open
            #   from the stack. 
            elif stack[-1] == parens[i]:
                stack.pop()

            # If the stack[-1] is not a matching open
            #   then its an invalid parenthesis
            else:
                return False
        
        # Else, add it to the stack
        else:
            stack.append(i)

    # If there is still an element in the stack
    #   then there is an open parenthesis left.
    if stack:
        return False

    return True


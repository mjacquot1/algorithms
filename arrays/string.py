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
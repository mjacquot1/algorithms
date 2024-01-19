def cut_ribbons(arr, k):
        def can_cut(arr, size, k):
            cut = 0

            for i in arr:
                cut += i // size
            
            return cut >= k

        low = 1
        high = max(arr)+1

        while low < high:
            mid = low + (high-low)//2

            if can_cut(arr, mid, k):
                low = mid + 1
            else:
                high = mid
        
        # Since were looking for the last working value
        # Decrment low by 1
        return low-1

def interval_intersections(arr_1, arr_2):
    ''' Return the intersection of two lists of intervals'''
    x, y = 0, 0
    ret_arr = []

    while x < len(arr_1) and y < len(arr_2):
        meeting_a = arr_1[x]
        meeting_b = arr_2[y]

        intersect_start = max(meeting_a[0], meeting_b[0])
        interect_end = min(meeting_a[1], meeting_b[1])

        if intersect_start <= interect_end:
            ret_arr.append([intersect_start, interect_end])

        if meeting_a[1] < meeting_b[1]:
            x += 1
        else:
            y += 1

    return ret_arr

def max_sub_array_val(nums):
    # Setup a max to return
    max_val = float('-inf')

    # Keep a running sum of values seen
    running_sum = 0

    for i in nums:
        # If i is decreased by the running sum
        #   then that means the running sum is negative.
        # You're better off restarting it at i
        if i >= (i + running_sum):
            running_sum = i
        else:
            running_sum += i
        
        max_val = max(running_sum, max_val)

    return max_val

def replace_element_with_greatest_on_right(arr):
    '''Replace every element in ans array with the greatest 
    element among the elements to its right, 
    and replace the last element with -1. '''

    # Start from the end, work to the beginning
    #   and keep track of the largest value youve seen
    max_right = -1

    for i in range(len(arr)-1, -1, -1):
        # Keep track of the current pointed value
        temp_val = arr[i]

        # Set the current pointed value
        #   to the max value seen so far
        arr[i] = max_right

        # Using temp_val, check if its the
        #   biggest val seen so far
        max_right = max(temp_val, max_right)

    return arr

def reverse_integer(x):
    ''' Given a signed 32-bit integer x, return x 
        with its digits reversed. If reversing x 
        causes the value to go outside the signed 
        32-bit integer range [-231, 231 - 1], 
        then return 0. '''

    # First, set the upper and lower 32bit bounds
    l_bound, u_bound = -2**31, 2**31-1

    # See if this value will need to be turned negative after
    conv = 1 if x >= 0 else -1

    # Convert x into a positive number and string
    val = str(abs(x))

    # Set up a return value
    ret_val = ''

    # Start from the end of val and walk backwards.
    #  This will reverse the string
    for i in range(len(val)-1, -1, -1):

        # Before you append the reveserd digit, 
        #   make sue it won't make it larger than a
        #   a 32 bit integer.
        if l_bound <= int(ret_val+val[i])*conv <= u_bound:
            ret_val += val[i]

        # If it does, return 0 
        else:
            return 0

    # Then convert it to an integer,
    #   and multiply it by conv in case
    #   it needs to be negative.            
    return int(ret_val)*conv

def happy_number_hash(num):
    ''' A happy number is if all it's chars squared and 
        summed equals 1 '''
    
    # Example 1:
    # Input: n = 19
    # Output: true
    # Explanation:
    # 12 + 92 = 82
    # 82 + 22 = 68
    # 62 + 82 = 100
    # 12 + 02 + 02 = 1


    # First create a set tracking values seen.
    # Start off with one, since thats true condition.
    seen = set({1})

    # Make a function to return the happy sum
    def happy_number(num):

        happy_sum = 0

        # Where going to keep finding the individual digit,
        #   squaring it, and summing it.
        while num > 0:
            # num % 10 only returns values < 10
            happy_sum += (num%10)**2
            # Shrink it down by a factor of 10.
            # // removes remainders
            num = num//10

        return happy_sum

    # Set the first sum
    curr_happy = happy_number(num)

    # Keep checking sums until you find a repeat
    while curr_happy not in seen:
        seen.add(curr_happy)
        curr_happy = happy_number(curr_happy)

    # Return if that repeat is equal to 1
    return curr_happy == 1
            
def happy_number_tortoise_hare(num):
    ''' A happy number is if all it's chars squared and 
        summed equals 1 '''
    
    # Example 1:
    # Input: n = 19
    # Output: true
    # Explanation:
    # 12 + 92 = 82
    # 82 + 22 = 68
    # 62 + 82 = 100
    # 12 + 02 + 02 = 1


    # First create a set tracking values seen.
    # Start off with one, since thats true condition.
    seen = set({1})

    # Make a function to return the happy sum
    def happy_number(num):

        happy_sum = 0

        # Where going to keep finding the individual digit,
        #   squaring it, and summing it.
        while num > 0:
            # num % 10 only returns values < 10
            happy_sum += (num%10)**2
            # Shrink it down by a factor of 10.
            # // removes remainders
            num = num//10

        return happy_sum

    # Set up a slow point and fast pointer.
    # The slow pointer will move process at a time.
    # The fast pointer will move two processes at a time,
    #   and eventually either reach the end or loop back
    #   around to the slow pointer because it is slowly
    #   closing the distance between the two.
    s_p = happy_number(num)
    f_p = happy_number(happy_number(num))


    while f_p != s_p:
        # Process the slow pointer once
        s_p = happy_number(s_p)

        # Process the fast poitner twice
        f_p = happy_number(happy_number(f_p))

    return f_p == 1
from collections import defaultdict, deque

from tests import peaks_valleys, strings, nums

from collections import deque
def permutation(q):
    if len(q) == 1:
        return [[q[0]]]

    result = []
    for i in range(len(q)):
        num = q.popleft()
        perms = permutation(q)

        for perm in perms:
            perm.append(num)
        result = result + perms
        
        q.append(num)
    print(result)
    return result

def buy_sell_stock(arr):
    # We are assuming 
    # you don't HAVE to buy
    max_profit = 0

    # set the left pointer to day 0
    l_point = 0

    # Start right pointer on the next day
    for r_point in range(1, len(arr)):
        # Keep seeing what the value would be if you bought at
        # the "lowest" point and sold at the current point.
        # Keep track of max profit you could get
        max_profit = max(arr[r_point]-arr[l_point], max_profit)
        
        # If you find a new "lowest" point
        # set l_point to that date.
        if arr[r_point] < arr[l_point]:
            l_point = r_point

    return max_profit

def max_profit_multiple(arr):
        ''' Find maximum profit with limitless trades'''
        # This requires a stock can be bought and sold
        # at the same price and same day
        if len(arr) <= 1:
            return 0

        profit = 0

        # Basically, if the price goes up
        # Assume we bought the day before,
        # and sold today.
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                profit += arr[i] - arr[i-1]

        return profit

def length_longest_substring_without_repeating(arr):
    if len(arr) <= 1:
        return len(arr)

    # Create a set to keep track
    # of chars in substring
    chars = set()

    # set the left pointer to 0
    l_point = 0

    # Start tracking max len of substrings
    max_substring = 0

    # move right pointer from 0 to end of arr
    for r_point in range(0,len(arr)):

        # While the current (r_point) char is in
        # the substring, shrink the window and
        # remove chararacters from the set
        # until the current char is not in the set.
        while arr[r_point] in chars:
            chars.remove(arr[l_point])
            l_point += 1
        
        # Add current char to the set
        chars.add(arr[r_point])

        # r_point-(l_point - 1) is the length of the current window
        # we do (l_point - 1) because if r_point == l_point
        # the window is the size of 1
        max_substring = max(r_point-(l_point-1), max_substring)
    
    return max_substring

def return_longest_substring_without_repeating(arr):
    if len(arr) == 0:
        return
    
    # Create a set to keep track
    # of chars in substring
    chars = set()

    # Keep track of largest substring length
    max_len = 0

    # Keep track of largest substring indexes
    largest_sub = (0, 0)

    # set the left pointer to 0
    l_point = 0

    for r_point in range(0, len(arr)):
        # While the current (r_point) char is in
        # the substring, shrink the window and
        # remove chararacters from the set
        # until the current char is not in the set.
        while arr[r_point] in chars:
            chars.remove(arr[l_point])
            l_point += 1
        
        # r_point-(l_point - 1) is the length of the current window
        # we do (l_point - 1) because if r_point == l_point
        # the window is the size of 1
        sub_len = r_point - (l_point-1)

        # is the current window is larger than previous longest
        if sub_len > max_len:
            # Set the largest_sub indexes to current window
            largest_sub = (l_point, r_point)
            # Replace largest sub length
            max_len = sub_len

        # Add current char to the set
        chars.add(arr[r_point])
    
    # Return the substring
    return arr[largest_sub[0]:largest_sub[1]+1]

def count_longest_substring_with_k_unique_chars(s, k):
    ''' Return largest substring len with at most k disctinct chars '''
    # If len(s) <= k
    # you can send it back
    if len(s) <= k:
        return len(s)

    # Set left pointer to 0
    l_point = 0

    # Set a max_len
    max_len = 0

    # Create a dictionary to hold the count
    # of unique characters in the sliding window
    window_chars = defaultdict(int)

    for r_point, r_char in enumerate(s):
        # Add the current char to the
        # count of unique windows characters
        window_chars[r_char] += 1

        # If the amount of unique characters
        # is greater than k, shrink window 
        if len(window_chars) > k:
            # Set l_char to equal the char that
            # l_point is pointing to
            l_char = s[l_point]
            
            # Reduce the count of the pointed char
            # in the whindows_char hash
            window_chars[l_char] -= 1

            # If the count of the character is 0
            # remove it from the dictionary
            # so it won't be coutned
            if window_chars[l_char] <= 0:
                window_chars.pop(l_char, None)

            # Increment l_point, and decrease the window
            l_point += 1

        # See if the window is the longest so far
        max_len = max(max_len, r_point-(l_point-1))

    return max_len

def count_longest_substring_with_k_replacements(s, k):
    ''' Find longest substring of repeating characters
    if you replace up to k characters with anything'''
    
    # len(s) <= k
    # you can replace all chars to match
    if len(s) <= k:
        return len(s)

    # Set left pointer to 0
    l_point = 0

    # Set a max_len
    max_len = 0

    # Create a dictionary to hold the count
    # of unique characters in the sliding window
    window_chars = defaultdict(int)

    # Start moving right pointer to the end
    for r_point, r_char in enumerate(s):
        # Add the current char to the
        # count of unique windows characters
        window_chars[r_char] += 1

        # We know the window is valid if
        # the length of the window minus the count of the most
        # matching characters is >= the substitutions you can make.
        # (IE you can replace the rest of the character to match)

        # If there are more non-matching characters than allowed
        # shrink the window until you need less than k substitutions.
        while (r_point - (l_point-1)) - max(window_chars.values()) > k:
            # Set l_char to equal the char that
            # l_point is pointing to
            l_char = s[l_point]
            
            # Reduce the count of the pointed char
            # in the whindows_char hash
            window_chars[l_char] -= 1

            # Increment l_point, and decrease the window
            l_point += 1

        # See if the window is the longest so far
        max_len = max(r_point - (l_point-1), max_len)

    return max_len

def find_anagrams_of_p(s, p):
    pass

def max_frequency(arr, k, *args):
    ''' return max values equal each other by incrementing
    other values by up to k in total increments'''

    # First sort.
    # We always need the largest value
    # on the rightmost side of the window
    arr.sort()
    
    # Keep track of the sum of values
    # in the window
    running_sum = 0

    # Keep track of the biggest
    # the window gets
    max_freq = 0

    # Set l_point to 0
    l_point = 0

    
    # What were going to do is see how much more
    # preceding values would need to be incremented
    # in order to equal the right-most value in the window
    for r_point, r_val in enumerate(arr):
        # Increase the running sum by
        # the current value
        running_sum += r_val


        # If r_point-l_point > 0, then the window is larger than
        # just 1 element.
        # Multiply the right-most value by the length of the window -1
        # to calculate how much the sum would be if all the values to
        # the left were equal to the right-most value.
        # Then subtract running_sum - r_val (we subtract r_val to remove
        # the right-most value).
        # If (sum of all left values if they were == right-most value) - (running_sum-r_val)
        # is greater than increments alotted to us, shrink the window and decrease running_sum.
        while r_val*(r_point-l_point) - (running_sum-r_val) > k:
            running_sum -= arr[l_point]
            l_point += 1
        
        # Check the biggest window so far
        max_freq = max(r_point-(l_point-1), max_freq)

    return max_freq


if __name__ == '__main__':
    # peaks_valleys(max_profit_multiple)
    # strings(count_longest_substring_with_k_unique_chars, 2)
    nums(max_frequency, 5)
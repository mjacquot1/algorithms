def two_sum(nums, target, *args):
    ''' Given an array of integers nums and a target,
        return indices of two numbers that add up to target '''   
    # Since we know the array is sorted, we can start from both ends
    #   and see if the value of the two pointed variables equal the
    #   target.
    # The idea behind this is that both ends together should equal
    #   more than the target, and we just need to either move down 
    #   (decrement) the sum or move up (increment) the sum until we 
    #   either find the values that equal the sum, of our pointers 
    #   meet and its impossible.

    # Start at both ends
    l_p, r_p = 0, len(nums)-1

    # We do '<' becuase if they ever meet,
    #   then only 1 number is actually being looked at
    while l_p < r_p:
        # Sum the pointed numbers
        curr_sum = nums[l_p] + nums[r_p]

        # Target is found!
        if curr_sum == target:
            return [l_p, r_p]

        # If the sum is less than the target,
        #   move up (increment) the smaller number
        elif curr_sum < target:
            l_p += 1
        # Else, move down (decrement) the larger number
        else:
            r_p -= 1

    return False



def move_zeroes(nums):
    ''' Given an integer array nums, move all 0's to the end of it while 
    maintaining the relative order of the non-zero elements. '''

    # If the there is only 1 or 0 elements
    #   its already done
    if len(nums) <= 1:
        return nums

    # Set 2 pointer, both starting at 0
    low, high = 0, 0

    # Start moving low up the array
    for low, val in enumerate(nums):
        # If it is zero, use 'high' to find
        # the next non-zero value to swap with
        if val == 0:
            
            # If high has fallen behind low
            #   set high to low
            high = max(high, low)

            # Move the high up until it finds a non-zero val
            while high < len(nums)-1 and nums[high] == 0:
                high += 1
            
            # Swap the zero val with the newly found non-zero val
            nums[low], nums[high] = nums[high], nums[low]
    
    return nums


def squares_of_sorted_array(nums):
    ''' Given an integer array nums sorted in non-decreasing order, 
    return an array of the squares of each number sorted in non-decreasing order. '''

    # If the array is sorted, and it has negatives
    #   the largest absolute values are on each end.

    # Start pointers from both ends
    l_point, r_point = 0, len(nums)-1

    # Set up array to return
    ret_arr = []    

    # Pointers will move towards eachother until 1 passes the other
    while l_point <= r_point:
        # Check the abs value on both ends
        l_val, r_val = abs(nums[l_point]), abs(nums[r_point])

        # If one is larger than the other, we know it will be the
        #   larger square. Append that to the array first.
        # Thenn move that pointer up or down the array.
        if l_val >= r_val:
            ret_arr.append(l_val*l_val) 
            l_point += 1

        elif r_val > l_val:
            ret_arr.append(r_val*r_val)
            r_point -= 1

    # Return the reversed array.
    return ret_arr[::-1]

def container_most_water(arr):
    ''' You are given an integer array height of length n. 
        There are n vertical lines drawn such that the two endpoints
        of the ith line are (i, 0) and (i, height[i]). 
        Find two lines that together with the x-axis form a container,
        such that the container contains the most water.'''

    # Set the max_container value found
    max_contained = float('-inf')

    # Set up a left pointer and right pointer
    #   to start at each end of the contianer
    l_point, r_point = 0, len(height) - 1

    # If the l_point and r_point meet eachother
    #   the container has a width of 0
    while l_point < r_point:
        l_val, r_val = arr[l_point], arr[r_point]
        
        # The container volume is going to equal
        #   (the smaller of the two sides)
        #   * (the distance between the 2 points)  
        container_volume = min(l_val, r_val)*(r_point-l_point)

        # set max_contained to the largest seen so far
        max_contained = max(container_volume, max_contained)

        # If l_val <= r_val, l_val is a chokepoint.
        # It is limiting the size of the container
        # Move l_point up by one.
        if l_val <= r_val:
            l_point += 1
        # Else, r_val is a chokepoint
        # It is limiting the size of the container
        # Move r_point down by one.
        else:
            r_point -= 1

    return max_contained

def trapping_rain_water_stack(arr):
    # Create a variable to track water trapped
    water_sum = 0

    # Create a stack that will hold
    #   for each value the (value, left_bound)
    temp_stack = []

    # Create variables to track the
    #   left and right bounds for each value
    max_left, max_right = 0, 0

    # Fill the temp_stack with each value
    #   and their left-most bound
    for val in arr:
        temp_stack.append((val, max_left))
        max_left = max(val, max_left)

    # Walk backards in the temp stack
    #   tracking the vlale and left-most bound
    for val, max_left in temp_stack[::-1]:
        # Water tha can be held is 
        #   (min of left and right bound) - val
        temp_water = min(max_left, max_right) - val
        
        # Add it to the sum if it is greater than 0
        water_sum += max(temp_water, 0)

        # See if the current value 
        #   is the new right-most bound
        max_right = max(val, max_right)

    return water_sum

def trapping_rain_water(arr):
    #Create a variable to track water trapped
    water_sum = 0


    # Create a variable to track the
    #   left and right bounds for each value
    l_point, r_point = 0, len(arr)-1

    # Create variables to track the
    #   left and right bounds for each value
    l_most, r_most = 0, 0

    # Once the left pointer crosses over the right pointer
    #   every value has been processed
    while l_point <= r_point:
        l_val, r_val = arr[l_point], arr[r_point]

        # Find out what the minimum bound is that determines
        #   how high the water can go.
        min_bound = min(l_most, r_most)

        # l_most <= r_most, l_most is the chokepoint
        #   keep processing how much water can be held
        #   until r_most is the chokepoint.
        if l_most <= r_most:
            # The water that can be held is the
            #   (minimum bound on either side) - (value at left pointer)
            water_sum += max((min_bound - l_val), 0)
            
            # Move up l_point.
            l_point += 1

        # l_most > r_most, r_most is the chokepoint
        #   keep processing how much water can be held
        #   until l_most is the chokepoint.
        elif l_most > r_most:
            # The water that can be held is the
            #   (minimum bound on either side) - (value at right pointer)
            water_sum += max((min_bound - r_val), 0)

            # Move down r_point.
            r_point -= 1

        # Keep track of the largest values seen through the
        #   left and right pointers
        l_most, r_most = max(l_val, l_most), max(r_val, r_most)

    return water_sum


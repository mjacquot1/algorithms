from tests import test_cases

def bubble_sort(arr, *args):
    for x in range(0, len(arr)):
        for i in range(0, len(arr)-1-x):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

def merge_sort_recursive(arr, low, high):
    def merge(arr, low, high):
        temp_arr = []
        
        mid = low + (high-low)//2
        
        left_p, right_p = low, mid+1
        
        # Create an in-order stack
        #  by comparing both sides using pointers
        while left_p <= mid and right_p <= high:
            if arr[left_p] <= arr[right_p]:
                temp_arr.append(arr[left_p])
                left_p += 1
            else:
                temp_arr.append(arr[right_p])
                right_p += 1
        
        # Add the rest of the values from the left side
        for i in range(left_p, mid+1):
            temp_arr.append(arr[i])
            
        # Add the rest of the values from the right side
        for i in range(right_p, high+1):
            temp_arr.append(arr[i])
        
        # Copy over the temp_arr values to the passed array
        for i in range(0, len(temp_arr)):
            # i+low because we are starting at low for arr
            # but starting at 0 for temp_arr
            arr[i+low] = temp_arr[i]
        
    mid = low + (high-low)//2
    
    # Base case is low < high
    if low < high:
        merge_sort_recursive(arr, low, mid)
        merge_sort_recursive(arr, mid+1, high)
        merge(arr, low, high)

def quick_sort_recursive(arr, low, high):
    ''' O(nlogn) usually, n^2 if in a reverse sorted array and pivot is 'high' '''
    
    def partition(arr, low, high):
        ''' Return pivot index '''
        
        # Choose middle element as pivot
        mid = low + (high-low)//2
        pivot = arr[mid]
        
        # The element we will swap with
        swap = low
        
        # Swap mid and high values
        # to get the pivot out of the way
        arr[mid], arr[high] = arr[high], arr[mid]
        
        # Go from low up until before the pivot
        # (which is now at index high)
        for i in range(low, high):
            # If arr[i] <= pivot, send it
            # to the swap and then swap += 1
            if arr[i] <= pivot:
                arr[i], arr[swap] = arr[swap], arr[i]
                swap += 1
        
        # Then swap the pivot between swap index and high
        # (We know arr[swap] > pivot by this point)
        arr[swap], arr[high] = arr[high], arr[swap]
    
        return swap
    
    # Base case is if low and high meet
    if low >= high:
        return
    
    # Get the middle point
    pivot_index = partition(arr, low, high)
    
    # Recurse on the left of the pivot
    quick_sort_recursive(arr, low, pivot_index-1)
    
    # Recurse on the right of the pivot
    quick_sort_recursive(arr, pivot_index+1, high)

def quick_sort_iterative(arr, *args):
    ''' O(nlogn) usually, n^2 if in a reverse sorted array and pivot is 'high' '''
    
    def partition(arr, low, high):
        ''' Return pivot index '''
        
        # Choose middle element as pivot
        mid = low + (high-low)//2
        pivot = arr[mid]
        
        # The element we will swap_index with
        # will start 1 before 'low'
        # And cover any 1 element arrays
        swap_index = low - 1
        
        # swap_index mid and high values
        # to get the pivot out of the way
        arr[mid], arr[high] = arr[high], arr[mid]
        
        # Go from low up until before the pivot
        # (which is now at index high)
        for i in range(low, high):
            # If arr[i] <= pivot, send it
            # to the swap_index index after swap_index += 1
            if arr[i] <= pivot:
                swap_index += 1
                arr[i], arr[swap_index] = arr[swap_index], arr[i]
                    # Increment swap_index one last time
                    
        # Then swap_index the pivot between swap_index index and high
        # (We know arr[swap_index] > pivot by this point)
        swap_index += 1
        arr[swap_index], arr[high] = arr[high], arr[swap_index]
    
        return swap_index
    
    # Declare the low & high here to start with
    low, high = 0, len(arr) - 1
    
    # Append the low & high as a tuple
    # We will be grabbing them and modifying them
    stack = [(low, high)]
    
    while stack:
        # Retrieve lo & high from the top of the stack
        low, high = stack.pop()
        
        # if low < high, then the sort window > 1 element
        if low < high:
            # Get the 'partition_index' where:
            # All to the left is < arr[partition_index]
            # all to the right is > arr[partition_index]
            partition_index = partition(arr, low, high)
            
            # Append the right window bounds
            stack.append((partition_index+1, high))
            
            # Append the left window bounds
            stack.append((low, partition_index-1))
        

def counting_sort(arr, max_k, *args):
    ''' Efficient when range of input data is not much bigger than
        the number of objects to be sorted '''

    # Create an array the size of the largest possible value + 1
    freq_arr = [0]*max_k+1

    # Create an array to hold sorted values.
    # Make it the length of passed array
    sorted_arr = [None]*len(arr)

    # Using the index, count how often a value is seen
    # Example: if i == 2, freq_arr[2] += 1 
    for i in arr: 
        freq_arr[i] += 1
    
    # Step through freq_arr, each value should equal
    # It's current count plus the previous element count
    for i in range(1, len(freq_arr)):
        freq_arr[i] = freq_arr[i] + freq_arr[i-1] 

    # Then step through arr.
    # And place values into new sorted array
    for i in arr:
        freq_arr[i] -= 1
        sorted_arr[freq_arr[i]] = i

    arr = sorted_arr

# test_cases(merge_sort_recursive)
# test_cases(bubble_sort)
test_cases(counting_sort, 10**5)




    


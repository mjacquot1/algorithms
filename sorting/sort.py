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

test_cases(merge_sort_recursive)
# test_cases(bubble_sort)




    


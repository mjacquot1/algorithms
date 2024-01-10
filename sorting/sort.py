from tests import test_cases

def merge_sort_recursive(arr, low, high):
    def merge(arr, low, high):
        mid = low + (high-low)//2

        temp_arr = []

        i = low
        j = mid + 1

        while i <= mid and j <= high:
            if arr[i] > arr[j]:
                temp_arr.append(arr[j])
                j += 1
            elif arr[i] <= arr[j]:
                temp_arr.append(arr[i])
                j += 1

        for i in range(i, mid+1):
            temp_arr.append(arr[i])

        for j in range(j, high+1):
            temp_arr.append(arr[j])

        for x in range(0, len(temp_arr)):
            arr[x+low] = temp_arr[x]
    
    mid = low + (high-low)//2

    if low < high:
        merge_sort_recursive(arr, low, mid)
        merge_sort_recursive(arr, mid+1, high)
        merge(arr, low, high)

test_cases(merge_sort_recursive)




    


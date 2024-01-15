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
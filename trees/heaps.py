import heapq
def k_clostest_point(points, k):
    def return_distance_from_z(x, y, z=(0,0)):
        return (x-z[0])**2 + (y-z[1])**2

    min_heap = []

    for i, (x, y) in enumerate(points):

        min_heap.append((return_distance_from_z(x, y), x, y))

    heapq.heapify(min_heap)

    ret_arr = []
    for i in range(k):
        dist, row, col = heapq.heappop(min_heap)

        ret_arr.append([row, col])

    return ret_arr
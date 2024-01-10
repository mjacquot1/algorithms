def test_cases(passed_function, *args):
    arrs = [
            [9,8,7,6,5,4,3,2,1,0],
            [1,2,5,6,7,3,5,6,7,8,0,2,3,4,6,2,2,7,4,5,7,8,0,2],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [5,4,3,2,1,0,-1,-2,-3,-4,-5],
            [2,1],
            [1,2],
            [0],
        ]
    
    
    
    for arr in arrs:
        passed_function(arr, 0, len(arr)-1)
        print(arr)
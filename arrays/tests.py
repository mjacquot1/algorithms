def peaks_valleys(passed_func, *args):
    arrs= [
        [8,6,4,3,3,2,3,5,8,3,8,2,6],
        [0,0,1],
        [0,1,1],
        [2,2,1],
        [2,1,1],
        [2,1,2],
        [1,2,1],
        [1,1,1],
        [1],
        [],
    ]

    for arr in arrs:
        print(passed_func(arr, *args))

def strings(passed_func, *args):
    arr=[
            "abcabcbb",
            "bbbbb",
            'bbbbbbabcb',
            'pwwkew',
            'a',
            ''
         ]
    
    for string in arr:
        print(passed_func(string, *args))

def nums(passed_func, *args):
    arrs = [
            [0,5,3,6,1,4,7,2,5,6,4,3],
            [0,1,2,3,4,5,6,7,8,9],
            [9,8,7,6,5,4,3,2,1,0],
            [0,0,0,0,1],
            [5,4,3,2,1,0,-1,-2,-3,-4,-5],
            [0,1],
            [1,0],
            [0],
            [],
         ]
    
    for arr in arrs:
        print(passed_func(arr, *args))
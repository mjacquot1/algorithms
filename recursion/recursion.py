def sum_all_integers(num, end):
    # Base case
    # If over the end, stop
    if num > end:
        return 0
    
    return (num + sum_all_integers(num + 1, end))

def unique_paths(matrix, row, col, end, path, ret_paths, visited):
    ''' Find all unique paths from start to end'''

    # This is easier for tracking the coordinate
    coord_string = f'{row},{col}'

    # Base cases
    # 1. The coordinate is out of bounds
    # 2. The coordinate has been visited
    # 3. The end is found
    if (row < 0 or row >= len(matrix)
            or col < 0 or col >= len(matrix[0])
            or coord_string in visited):
        return
    
    # End is found
    if row == end[0] and col == end[1]:
        # Create a string for the path, add the end coordinate to it
        # then append it to the return paths
        ret_paths.append(' -> '.join(path) + f' -> {coord_string}')
        # Then return to skip the end coordinate
        return

    # Add the current coordinate to the working path
    # And add it to the visited paths
    path.append(f'{row},{col}')
    visited.add(coord_string)

    # Try going up, down, left, and then right
    unique_paths(matrix, row-1, col, end, path, ret_paths, visited)
    unique_paths(matrix, row+1, col, end, path, ret_paths, visited)
    unique_paths(matrix, row, col-1, end, path, ret_paths, visited)
    unique_paths(matrix, row, col+1, end, path, ret_paths, visited)

    # Now were backtracking, remove the current coord from
    # the current path, and visited paths
    path.pop()
    visited.remove(coord_string)

def count_unique_paths(matrix, row, col, end, visited):

    coord_string = f'{row},{col}'

    # Base Cases
    # 1. Coordinate is out of bounds
    # 2. Coordinate is in visited
    # 3. End is found

    if (row < 0 or col < 0
            or row >= len(matrix) or col >= len(matrix[0])
            or coord_string in visited):
        return 0
    
    if row == end[0] and col == end[1]:
        return 1
    
    visited.add(coord_string)

    ret_val = (
        count_unique_paths(matrix, row+1, col, end, visited)
        + count_unique_paths(matrix, row-1, col, end, visited)
        + count_unique_paths(matrix, row, col+1, end, visited)
        + count_unique_paths(matrix, row, col-1, end, visited)
    )

    visited.remove(coord_string)

    return ret_val

def top_left_bottom_right_unique_paths_contstrained(rows, cols):
    ''' Count unique paths if you can only move down and right '''
    # Assume the count of elements is passed, not indexes
    # If the last col or last row is reached, return 1
    if rows == 1 or cols == 1:
        return 1
    

    return (top_left_bottom_right_unique_paths_contstrained(rows-1, cols)
            + top_left_bottom_right_unique_paths_contstrained(rows, cols-1))

def string_reversal(s, i=0):
    # Base case:
    # 1. i >= len(str)
    if i >= len(s):
        return ''
    
    return (string_reversal(s,i+1) + s[i])

def array_reversal(arr):

    # Base case:
    # len(arr) == 0:
    if len(arr) == 1:
        return arr
    
    elem = arr.pop()

    return (array_reversal(arr) + [elem])

def is_palindrome(s):
    # Keep shrinking the string by the ends
    # Check to see if s[0] == s[-1]

    # Base cases
    # 1. The string is reduced to 1 or 0 len
    #       (This means pointers have met)
    # 2. s[0] != s[-1]

    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    # Keep shrinking
    return is_palindrome(s[1:-1])


# print(sum_all_integers(-4, 5))
matrix = [
    ['S','',''],
    ['','',''],
    ['','','E'],
]

arr = [0,1,2,3,4,5,6,7,8,9]
str = '1,2,3,4,5,6,7,8,9,0'
print(string_reversal(str))
# print (array_reversal(arr))

palins = [
    'aba',
    'aa',
    'a',
    '',
    'baa',
]

for i in palins:
    print(is_palindrome(i))

# ret_paths = []
# unique_paths(matrix, 0, 0, (0,0), [], ret_paths, set())
# print(len(ret_paths))
# print(count_unique_paths(matrix, 0, 0, (0,0), set()))
# print(top_left_bottom_right_unique_paths_contstrained(len(matrix), len(matrix[0])))

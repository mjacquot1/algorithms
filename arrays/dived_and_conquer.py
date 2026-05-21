def longestCommonPrefix(self, strs: List[str]) -> str:
  def least_common_prefix(left, right):
    print(right, left)
    min_len = min(len(left), len(right))
    prefix = ''
    for i in range(0, min_len):
      if left[i] == right[i]:
        prefix += left[i]
      else:
        return prefix
    return prefix

def divide_conquer(arr, l, r):
    if l == r:
      print(arr[l])
      return arr[l]
    
    mid = ( r + l ) // 2
    left = divide_conquer(arr, l, mid)
    right = divide_conquer(arr, mid+1, r)
    return least_common_prefix(left, right)

return divide_conquer(strs, 0, len(strs)-1)
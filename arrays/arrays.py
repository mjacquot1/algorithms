from collections import deque
def permutation(q):
    if len(q) == 1:
        return [[q[0]]]

    result = []
    for i in range(len(q)):
        num = q.popleft()
        perms = permutation(q)

        for perm in perms:
            perm.append(num)
        result = result + perms
        
        q.append(num)
    print(result)
    return result

q = deque([1,2,3])
print(permutation(q))
    




    

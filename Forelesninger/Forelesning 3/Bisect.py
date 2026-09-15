# My implementation of binary search 
import math

def bisect(A, v, low=0, high=None):
    """
        A = Sortet list
        v = value we want to find
        low = lowest index
        high = highest index
    """

    if high is None: 
        high = len(A) - 1
    
    if low <= high: 
        q = (low + high) // 2
        if A[q] == v:
            return q 
        elif v < A[q]:
            return bisect(A, v, low, q-1)
        else:
            return bisect(A, v, q + 1, high)
    return None

l = [n for n in range (10)]

print(bisect(l, 6))

        
        
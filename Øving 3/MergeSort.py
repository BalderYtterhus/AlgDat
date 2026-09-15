def merge(A, low, mid, high:int):
    """
        Takes an array A, splits in two and sorts
    """

    L = A[low : mid + 1]
    R = A[mid + 1 : high + 1]

    i = 0
    j = 0

    for k in range (high):
        


def merge_sort(A, low=0, high=None):
    """
        Takes an Array A, finds its midpoint -> sort/merges recursively
    """

    if high is None: 
        high = len(A) - 1

    mid = (high + low) // 2

    merge_sort(A, low, mid)
    merge_sort(A, mid, high)

    merge(A, low, mid, high)
    

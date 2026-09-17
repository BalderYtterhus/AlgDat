# Merge sort 
def merge_sort(A:list , p:int, r=None) -> None:
    if p >= r:
        return 

    q = (p + r) // 2

    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)

    merge(A, p, q, r)

def merge(A:list, p:int, q:int, r:int) -> None:
    n1 = q - p + 1 
    n2 = r - q 

    l1 = [0 for n in range(n1)] 
    l2 = [0 for n in range(n2)] 

    for i in range(n1):
        l1[i] = A[p + i]
    for i in range(n2):
        l2[i] = A[q + i + 1]

    i = 0
    j = 0
    k = p

    while i < n1 and j < n2:
        if l1[i] <= l2[j]:
            A[k] = l1[i]
            i += 1
        else:
            A[k] = l2[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = l1[i]
        k += 1
        i += 1
    while j < n2: 
        A[k] = l2[j]
        k += 1
        j += 1
def k_largest(A, n, k):
    if k == 0 or n == 0:
        return []
    
    m = get_pivot(A) # Riktig pivot

    smaller = []
    bigger = []
    equal_count = 0

    for num in A:
        if num < m:
            smaller.append(num)
        elif num > m:
            bigger.append(num)
        else:
            equal_count += 1

    if len(bigger) == k: 
        return bigger
    
    if len(bigger) < k:     
        diff = k - len(bigger)

        take_equal = min(diff, equal_count)
        bigger.extend([m] * take_equal)
        diff -= take_equal

        if diff == 0:
            return bigger

        remaining_largest = k_largest(smaller, len(smaller), diff)
        bigger.extend(remaining_largest)

        return bigger


    if len(bigger) > k:
        return k_largest(bigger, len(bigger), k)

def insertion_sort(A):

    for i in range(1, len(A)):
        key = A[i]

        j = i - 1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

    return A

def find_median(A):
    insertion_sort(A)
    return A[len(A) // 2]

def get_pivot(A):
    medians = []

    for i in range(0, len(A), 5):
        group = A[i:i + 5]
        medians.append(find_median(group))

    if len(medians) <= 5:
        return find_median(medians)

    return get_pivot(medians)
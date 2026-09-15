def insertion_sort(A, n):

    for i in range(1, n):
        key = A[i]

        j = i - 1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

    return A

A = [6, 7, 3, 4, 5, 1, 2]
print(insertion_sort(A, len(A)))

        
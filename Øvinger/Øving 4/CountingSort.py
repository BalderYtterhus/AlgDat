def counting_sort(A: list, n: int) -> list:
    if len(A) == 0:
        return []
    
    C = [0] * (max(A) + 1) # Makes an empty list with the right amount of elements

    for number in A:
        C[number] += 1 # Counts how many of the numbers there is

    B = [] # Empty list b for return

    for number, count in enumerate(C): # Gets number/index and their count
        for _ in range(count): # Appends as many as count of the given number
            B.append(number)

    return B


p = [1, 4, 3, 6, 8, 5, 9]
k = 2

def m(n):
    if n == 0:
        return 0
    
    best = -1

    for i in range(1, n + 1):
        best = max(best, p[i - 1] + m(n-i) - k)

    return best 

print(m(7))

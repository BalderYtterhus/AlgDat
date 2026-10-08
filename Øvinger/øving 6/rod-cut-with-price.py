p = [1, 4, 3, 6, 8, 5, 9]
k = 2

def m(n):
    r = [0]*(n+1)

    if n == 0:
        return 0
    

    for i in range(1, n + 1):
        best = p[i - 1]

        for j in range(1, i):
            best = max(best, p[j - 1] + r[i-j] - k) 
        r[i] = best
    
    return r[n] 

print(m(7))

def prefix_sums(A):
    n = len(A)
    P = [0] * (n+1)

    for x in range(1, n+1):
        P[x] = P[x-1] + A[x-1]
    
    return P

print(prefix_sums([1,2,3,4]))

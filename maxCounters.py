def solution(N, A):
    arr = [0] * len(A)
    num = N

    for x in A:
        if 1 <= x <= N:
            arr[x] += 1
    
    return arr

print(solution(5, [3,4,4,6,1,4,4]))

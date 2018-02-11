def solution(A):
    arrF = A[0]
    mini = 0
    res = 0
    
    for x in range(1, len(A)):
        res += A[x]

    mini = abs(arrF - res)

    for y in range(1, len(A)):
        arrF += A[y]
        res -= A[y]
        if abs(arrF - res) < mini:
            mini = abs(arrF - res)

    return mini

print(solution([3,1,2,4,3]))

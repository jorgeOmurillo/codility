def solution(A):
    suma = 0

    for x in range(len(A)):
        suma += ((x + 1) - A[x])

    return suma + (len(A) + 1)

print(solution([2,5,1,4]))

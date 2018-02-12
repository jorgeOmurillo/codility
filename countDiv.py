def solution(A, B, K):
    a = A//K
    b = B//K

    if A % K == 0:
        a -= 1

    return b-a

print(solution(6, 11, 2))

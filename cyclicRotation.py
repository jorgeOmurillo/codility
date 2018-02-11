def solution(A, K):
    num = K

    while num > 0:
        A.insert(0, A.pop())
        num -= 1

    return A

print(solution([3, 8, 9, 7, 6], 3))
print(solution([1, 2, 3, 4], 4))

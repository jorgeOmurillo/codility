def solution(A):
    arr = [0] * (len(A))

    for x in A:
        if 1 <= x <= len(A):
            arr[x-1] = 1

    for y in range(len(arr)):
        if arr[y] == 0:
            return y+1

    return -1

print(solution([1, 3, 6, 4, 1, 2]))
print(solution([-1, -3]))

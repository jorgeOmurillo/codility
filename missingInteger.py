def solution(A):
    length = len(A)+1
    arr = [0] * length

    for x in A:
        if 1 <= x <= length:
            arr[x-1] = 1

    for y in range(length):
        if arr[y] == 0:
            return y+1

    return -1

print(solution([1,3,6,4,1,2]))
print(solution([1,2,3]))
print(solution([-1,-3]))

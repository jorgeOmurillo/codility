def solution(N, A):
    arr = [0] * N
    maxCounter = 0
    smallCounter = 0

    for x in A:
        if 1 <= x <= N:
            if arr[x-1] < maxCounter:
                arr[x-1] = maxCounter

            arr[x-1] += 1

            if arr[x-1] > smallCounter:
                smallCounter = arr[x-1]
        else:
            maxCounter = smallCounter


    for y in range(len(arr)):
        if arr[y] < maxCounter:
            arr[y] = maxCounter
    
    return arr

print(solution(5, [3,4,4,6,1,4,4]))

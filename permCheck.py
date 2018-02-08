# def solution(X, A):
    # arr = [0] * X
    # num = X

    # for x in range(len(A)-1):
        # if arr[A[x]-1] == 0:
            # arr[A[x]-1] = A[x]
            # num -= 1
        # if num == 0:
            # return x
    
    # return -1

# print(solution(5, [1,3,1,4,2,3,5,4]))

def solution(A):
    arr = [0] * len(A)

    for x in range(len(A)):
        if A[x] > len(A):
            return 0
        else:
            if arr[A[x]-1] == A[x]:
                return 0
            if arr[A[x]-1] == 0:
                arr[A[x]-1] = A[x]

    return 1

print(solution([4,1,3,0]))

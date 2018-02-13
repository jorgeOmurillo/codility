def solution(A):
    counted = 0
    cars = 0

    for x in range(len(A)):
        if A[x] == 0:
            counted += 1
        if counted > 0 and A[x] == 1:
            cars += counted
        if cars > 1000000000:
            return -1
    
    return cars

print(solution([0,1,0,1,1]))

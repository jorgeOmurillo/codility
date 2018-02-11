def solution(N):

    text = "{0:b}".format(N)
    temp = 0
    binG = 0

    for x in text:
        if x == "0":
            binG += 1
        if x == "1":
            if binG > temp:
                temp = binG
            binG = 0

    return temp

print(solution(1041))

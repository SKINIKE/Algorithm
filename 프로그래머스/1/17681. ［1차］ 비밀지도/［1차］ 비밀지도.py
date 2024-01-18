def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 =[]
    for i in arr1:
        map1.append(format(i, 'b').zfill(n))
    for i in arr2:
        map2.append(format(i, 'b').zfill(n))
    for i in range(n):
        tmp = []
        for j in range(n):
            if map1[i][j] == "1" or map2[i][j] == "1":
                tmp.append("#")
            else:
                tmp.append(" ")
        answer.append(''.join(tmp))
    return answer
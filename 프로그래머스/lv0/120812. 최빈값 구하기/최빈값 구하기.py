def solution(array):
    a = set(array)
    cntArray = [array.count(i) for i in a]
    if cntArray.count(max(cntArray)) > 1:
        return -1    
    for x in a:
        if array.count(x) == max(cntArray):
            return x
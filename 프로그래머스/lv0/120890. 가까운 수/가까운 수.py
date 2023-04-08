def solution(array, n):
    a = {} 
    b = 9999
    for i in array:
        if abs(i-n) in a:
            if a[abs(i-n)] > i:
                a[abs(i-n)] = i
        else:
            a[abs(i-n)] = i
                
        if abs(i-n) < b:
            b = abs(i-n)
    return a[b]
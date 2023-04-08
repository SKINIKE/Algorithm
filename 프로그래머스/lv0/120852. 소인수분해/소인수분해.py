def solution(n):
    i = 2
    a = []
    
    while n > i:
        if n % i == 0:
            n = n // i
            a.append(i)
        else:
            i += 1
    a.append(i)
    return sorted(list(set(a)))
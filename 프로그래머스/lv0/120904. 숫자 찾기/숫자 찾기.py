def solution(num, k):
    a = [i[0] for i in enumerate(str(num)) if i[1] == str(k)]
    return a[0]+1 if len(a) > 0 else -1
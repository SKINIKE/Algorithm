def solution(emergency):
    a = emergency.copy()
    for i, j in enumerate(sorted(emergency, reverse=True)):
        a[emergency.index(j)] = i+1
    return a
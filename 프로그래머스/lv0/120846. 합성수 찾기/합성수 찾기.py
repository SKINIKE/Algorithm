def solution(n):
    a = []
    for i in range(1, n + 1):
        b = [j for j in range(1, i + 1) if (i) % j == 0]
        if len(b) >= 3:
            a.append(b)
    return len(a)
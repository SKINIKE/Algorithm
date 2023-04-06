def solution(num_list, n):
    a = num_list.copy()[::-1]
    b = []
    c = []
    for i in range(len(num_list) // n):
        for i in range(n):
            b.append(a.pop())
        c.append(b)
        b = []
    return c
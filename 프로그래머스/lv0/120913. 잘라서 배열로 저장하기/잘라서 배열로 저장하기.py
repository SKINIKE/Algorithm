import math

def solution(my_str, n):
    a = 0
    b = []
    for i in range(1, math.ceil(len(my_str) / n) + 1):
        b.append(my_str[a:i*n])
        a = i * n
    return b
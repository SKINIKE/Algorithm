import math

def solution(n):
    a = [math.factorial(i) for i in range(1, 11)]
    return a.index(max([i for i in a if i <= n])) + 1
import sys

sys.setrecursionlimit(10**7)

arr = [0] * 1000000

def solution(n):
    if n == 1 or n == 2:
        return 1
    if arr[n] != 0:
        return arr[n]
    arr[n] = solution(n - 1) + solution(n - 2)
    return arr[n] % 1234567
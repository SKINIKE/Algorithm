def solution(n):
    return ((n ** (1 / 2)) + 1) * ((n ** (1 / 2)) + 1) if n ** (1 / 2) % 1 == 0 else -1
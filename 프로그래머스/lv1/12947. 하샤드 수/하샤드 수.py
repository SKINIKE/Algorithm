def solution(x):
    return True if x % sum([int(a) for a in str(x)]) == 0 else False
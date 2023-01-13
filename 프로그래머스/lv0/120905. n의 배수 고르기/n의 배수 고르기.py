def solution(n, numlist):
    return [x for x in numlist if divmod(x, n)[1] == 0]
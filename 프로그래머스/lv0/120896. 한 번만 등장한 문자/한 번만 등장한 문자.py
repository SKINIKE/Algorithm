def solution(s):
    return ''.join(sorted([ x for x in list(s) if list(s).count(x) == 1]))
     
def solution(s1, s2):
    answer = 0
    for x in s1:
        if s2.count(x) > 0:
            answer += 1
    return answer
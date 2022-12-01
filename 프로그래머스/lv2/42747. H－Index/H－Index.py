def solution(citations):
    answer = 0
    for i in sorted(citations, reverse = True):
        if i > sorted(citations, reverse = True).index(i)+1:
            answer = sorted(citations, reverse = True).index(i)+1
    return answer
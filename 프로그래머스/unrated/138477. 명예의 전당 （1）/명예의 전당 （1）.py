def solution(k, score):
    answer = []
    minScore = []
    for i in score:
        if len(minScore) < k:
            minScore.append(i)
        else:
            minScore.sort()
            if i > minScore[0]:
                minScore.append(i)
                del minScore[0]
        answer.append(min(minScore))
    return answer
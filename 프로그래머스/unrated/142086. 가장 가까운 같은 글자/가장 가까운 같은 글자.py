def solution(s):
    answer = []
    reS = s[::-1]
    for idx, val in enumerate(reS):
        x = reS[idx+1:].find(val)
        answer.append(x) if x == -1 else answer.append(x + 1)
    return answer[::-1]
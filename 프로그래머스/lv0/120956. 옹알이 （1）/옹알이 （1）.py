from itertools import *

def solution(babbling):
    baby = ["aya", "ye", "ma", "woo"]
    answer = []
    cnt = 0
    
    for i in range(len(baby)):
        answer.append([''.join(x) for x in list(product(baby, repeat= i + 1))])
    
    answer2 = list(chain.from_iterable(answer))

    for x in babbling:
        ansCnt = answer2.count(x)
        if ansCnt > 0:
            cnt += ansCnt
    
    return cnt
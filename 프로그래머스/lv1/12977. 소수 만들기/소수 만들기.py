from itertools import combinations

def solution(nums):
    answer = 0
    candi = list(combinations(nums, 3))
    
    for i in  candi:
        si = sum(i)
        pn = True
        for j in range(2, si):
            if si % j == 0:
                pn = False
        if pn:
            answer += 1
    return answer
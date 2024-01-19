def solution(n):
    answer = 0
    sjs = []
    
    while(divmod(n, 3)[0] != 0):
        tp = divmod(n, 3)
        sjs.append(tp[1])
        n = tp[0]
    sjs.append(n % 3)
    
    for idx, val in enumerate(sjs[::-1]):
        answer += (3**idx) * val
        
    return answer
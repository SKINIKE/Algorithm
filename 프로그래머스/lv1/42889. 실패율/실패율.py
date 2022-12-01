def solution(N, stages):
    stages_err = {}
    user = len(stages)
    
    for i in range(N):
        stages_err[i+1] = stages.count(i+1)
    
    for i in stages_err:
        if user != 0:
            err = stages_err[i] / user
            user -= stages_err[i]
            stages_err[i] = err
        else:
            stages_err[i] = 0
    return sorted(stages_err, key= lambda x : stages_err[x], reverse=True)
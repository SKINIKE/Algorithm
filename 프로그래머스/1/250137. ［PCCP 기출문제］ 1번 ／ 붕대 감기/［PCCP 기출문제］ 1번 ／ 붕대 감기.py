def solution(bandage, health, attacks):
    curHealth = health
    success = 0
    
    for i in range(attacks[-1][0]):
        cnt = i + 1
        if(cnt == attacks[0][0]):
            curHealth -= attacks[0][1]
            success = 0
            if curHealth <= 0:
                return -1
            del attacks[0]
        else:
            curHealth += bandage[1]
            success += 1
            if(success == bandage[0]):
                curHealth += bandage[2]
                success = 0
            if(curHealth >= health):
                curHealth = health    
    return curHealth
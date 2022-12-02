def solution(s):
    answer = True
    s = s.lower()
    pcnt = list(s).count("p")
    ycnt = list(s).count("y")

    if pcnt != ycnt:
        return False
    
    return True
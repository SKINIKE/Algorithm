def solution(rsp):
    table = str.maketrans("025", "502")
    return rsp.translate(table)
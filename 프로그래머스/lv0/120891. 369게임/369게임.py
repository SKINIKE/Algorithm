def solution(order):
    return len([x for x in list(str(order)) if x in ["3", "6", "9"]])
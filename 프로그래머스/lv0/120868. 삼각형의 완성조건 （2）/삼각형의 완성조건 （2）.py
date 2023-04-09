def solution(sides):
    return (max(sides) - (max(sides) - min(sides))) + ((sum(sides) -1) - max(sides))
def solution(my_string):
    return sum([int(x) for x in list(my_string) if x.isdigit()])
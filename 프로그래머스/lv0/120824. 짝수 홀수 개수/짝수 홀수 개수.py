def solution(num_list):
    a = len([x for x in num_list if x % 2 == 0])
    b = len([x for x in num_list if x % 2 != 0])
    return [a, b]
def solution(my_string, letter):
    return ''.join([x for x in list(my_string) if x != letter])
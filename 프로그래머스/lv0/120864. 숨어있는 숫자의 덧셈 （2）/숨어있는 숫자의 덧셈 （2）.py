import re

def solution(my_string):
    a = re.split('[a-zA-Z]', my_string)
    return sum([int(x) for x in a if x])
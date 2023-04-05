import string

def solution(age):
    return ''.join([list(string.ascii_lowercase)[int(i)] for i in list(str(age))])
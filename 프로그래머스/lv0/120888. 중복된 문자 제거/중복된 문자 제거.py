def solution(my_string):
    a = [] 
    [a.append(i) for i in list(my_string) if i not in a]
    return ''.join(a)
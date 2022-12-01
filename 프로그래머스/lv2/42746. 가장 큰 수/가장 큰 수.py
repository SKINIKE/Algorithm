def solution(numbers):
    answer = ''
    num = [str(x) for x in numbers]
    num.sort(key=lambda num: num*3, reverse=True) 
    for n in num: answer += n
    return str(int(answer))
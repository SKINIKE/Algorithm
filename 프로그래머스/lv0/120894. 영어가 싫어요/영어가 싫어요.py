def solution(numbers):
    a = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i, j in enumerate(a):
        numbers = numbers.replace(j, str(i))
    return int(numbers)
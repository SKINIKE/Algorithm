import math

def solution(denum1, num1, denum2, num2):
    answer = []
    lcm = num1 * num2 // math.gcd(num1, num2)
    i = (denum1 * (lcm // num1)) + (denum2 * (lcm // num2))
    gcd = math.gcd(i, lcm)
    answer.append(i//gcd)
    answer.append(lcm//gcd)
    return answer
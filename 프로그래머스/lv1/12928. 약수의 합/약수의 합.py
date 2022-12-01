def solution(n):
    answer = []
    for i in range(1, n + 1):
        if i > n / 2:
            answer.append(n)
            break
        elif n % i == 0:
            answer.append(i)
    return sum(answer)
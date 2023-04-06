def solution(numbers, k):
    a = 0

    for i in range(0, k * 2, 2):
        if i > len(numbers) - 1:
            a = i % len(numbers)
        else:
            a = i
    return numbers[a]
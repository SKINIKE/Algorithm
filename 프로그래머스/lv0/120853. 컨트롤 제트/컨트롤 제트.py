def solution(n):
    b = []
    for i in n.split(" "):
        b.pop() if i == 'Z' else b.append(int(i))
    return sum(b)
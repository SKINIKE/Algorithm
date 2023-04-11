from collections import deque

def solution(A, B):
    c = []
    dq = deque(A)
    for i in range(len(dq)):
        d = dq.pop()
        dq.appendleft(d)
        c.append(''.join(dq))
    if A == B:
        return 0
    elif B in c:
        return c.index(B) + 1
    else:
        return -1
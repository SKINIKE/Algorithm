def solution(cipher, code):
    return ''.join([c for i, c in enumerate(list(cipher)) if (i+1) % code == 0])
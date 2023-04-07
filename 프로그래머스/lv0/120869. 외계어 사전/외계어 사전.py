from itertools import permutations

def solution(spell, dic):
    return 1 if len([i for i in permutations(spell, len(spell)) if ''.join(i) in dic]) > 0 else 2
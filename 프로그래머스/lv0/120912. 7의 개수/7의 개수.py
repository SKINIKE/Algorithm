def solution(array):
    return sum([list(x).count("7") for x in [str(s) for s in array]])
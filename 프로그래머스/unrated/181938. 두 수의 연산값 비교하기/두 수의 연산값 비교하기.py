def solution(a, b):
    aa = int(str(a) + str(b))
    bb = 2 * a * b
    if aa >= bb:
        return aa
    elif aa < bb:
        return bb
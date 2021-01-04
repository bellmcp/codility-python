# Count Div
from math import floor, ceil


def solution(A, B, K):
    n_start = ceil(A / K)
    n_end = floor(B / K)
    return n_end - n_start + 1


print(solution(6, 11, 2))
print(solution(11, 345, 17))

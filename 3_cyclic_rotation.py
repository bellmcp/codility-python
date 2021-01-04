# cyclic rotation

def solution(A, k):
    result = [None] * len(A)
    for i in range(0, len(A)):
        result[(i+k) % len(A)] = A[i]
    return result


print(solution([1, 2, 3, 4, 5], 2))
print(solution([1, 2, 3, 4, 5], 5))

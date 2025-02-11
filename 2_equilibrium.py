# Tape Equilibrium

def solution(A):
    sum_left = A[0]
    sum_right = sum(A) - A[0]
    diff = abs(sum_left - sum_right)

    for i in range(1, len(A) - 1):
        sum_left += A[i]
        sum_right -= A[i]
        current_diff = abs(sum_left - sum_right)
        if (current_diff < diff):
            diff = current_diff

    return diff


print(solution([3, 1, 2, 4, 3]))
print(solution([1, 2, 3]))

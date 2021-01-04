# Max Profit

def solution(A):
    global_max_sum = 0
    local_max_sum = 0

    for i in range(1, len(A)):
        delta = A[i] - A[i-1]
        local_max_sum = max(delta, local_max_sum + delta)
        global_max_sum = max(local_max_sum, global_max_sum)

    return global_max_sum


print(solution([23171, 21011, 21123, 21366, 21013, 21367]))

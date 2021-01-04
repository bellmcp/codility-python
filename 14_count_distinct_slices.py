# Count Distinct Slices

def solution(M, A):
    total_slices = 0
    in_current_slices = [False] * (M + 1)
    head = 0

    for tail in range(0, len(A)):
        while head < len(A) and (not in_current_slices[A[head]]):
            in_current_slices[A[head]] = True
            total_slices += (head-tail) + 1
            head += 1
            total_slices = 1000000000 if total_slices > 1000000000 else total_slices

        in_current_slices[A[tail]] = False

    return total_slices


print(solution(6, [3, 4, 5, 5, 2]))

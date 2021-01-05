# Leader

def solution(A):
    consecutive_size = 0
    candidate = 0

    for item in A:
        if consecutive_size == 0:  # stack is empty
            candidate = item
            consecutive_size += 1
        elif candidate == item:  # found matched
            consecutive_size += 1
        else:  # found unmatched
            consecutive_size -= 1

    occurrence = A.count(candidate)

    if occurrence > (len(A) / 2):  # check is leader
        return A.index(candidate)  # return (any) index
    else:
        return -1


print(solution([3, 0, 1, 1, 4, 1, 1]))

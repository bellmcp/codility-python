# Max Counter
def solution(N, A):
    counters = [0] * N
    start_line = 0
    current_max = 0

    for i in A:
        x = i - 1
        if (i > N):  # max-counter
            start_line = current_max
        elif (counters[x] < start_line):  # behind start line
            counters[x] += start_line + 1
        else:  # ahead start line
            counters[x] += 1
        if (i <= N and counters[x] > current_max):  # update current max
            current_max = counters[x]

    for i in range(0, N):  # move counter behind start line to start line
        if (counters[i] < start_line):
            counters[i] = start_line

    return counters


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))

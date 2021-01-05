# Fish

def solution(A, B):
    stack = []
    survivors = 0

    for i in range(len(A)):
        weight = A[i]

        if B[i] == 1:  # downsteam = 1
            stack.append(weight)
        else:  # upsteam compare with fish in stack
            # stack is not empty if empty weightdown = -1
            weightdown = stack.pop() if stack else -1

            while weightdown != -1 and weightdown < weight:  # not empty and fish in stack is smaller
                weightdown = stack.pop() if stack else -1

            if weightdown == -1:  # when stack is empty > increase survivor
                survivors += 1
            else:  # when the fish in stack wins > push back to stack
                stack.append(weightdown)

    return survivors + len(stack)  # survivors + fish left in stack


print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))

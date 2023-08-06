from collections import deque

def solution(arr):
    answer = []

    dq = deque(arr)
    answer.append(dq.popleft())
    
    for num in dq:
        if num != answer[-1]:
            answer.append(num)

    return answer

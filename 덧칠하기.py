'''
54점 코드

from collections import deque

def solution(n, m, section):
    answer = 0
    
    dq = deque([])
    for i in range(section[0], section[len(section)-1]+1):
        # print(i)
        dq.append(i)
    # print(dq)
    
    while dq:
        dq.popleft()
        answer += 1
    
    if answer % m == 0:
        return answer // m
    return (answer // m) + 1
'''

# 엇코드 - 아직 익숙치 않다.
def solution(n, m, section):
    answer = 0
    last = 0
    
    for elem in section:
        if elem > last:
            answer += 1
            last = elem + m - 1 
    
    return answer
    

# 1>0-1, 2>1-2, 3>2-3, 4>3-4 --> answer = 4

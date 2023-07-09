# Counter 함수 사용
from collections import Counter

def solution(X, Y):
    answer = ''
    
    x = Counter(X)
    y = Counter(Y)
    common = x - (x - y)
    # print(x, y, common)
    
    for key, value in common.items():
        answer += key * value
        answer = sorted(answer, reverse=True)
        answer = ''.join(answer)
    # print(answer)
    
    if not answer:
        return '-1'
    elif answer.startswith('0'):
        return '0'
    else:
        return answer
    
    

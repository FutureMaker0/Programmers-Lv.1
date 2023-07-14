def solution(a, b):
    answer = 0
    
    result = zip(a, b)
    result = list(result)
    
    for case in result:
        answer += (case[0] * case[1])
    
    return answer

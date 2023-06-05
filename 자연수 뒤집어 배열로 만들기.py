def solution(n):
    answer = []
    
    n2 = str(n)[::-1]
    
    for num in n2:
        answer.append(int(num))
    
    return answer

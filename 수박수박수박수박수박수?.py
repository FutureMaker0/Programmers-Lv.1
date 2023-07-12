def solution(n):
    answer = ''
    temp = []
    
    for i in range(1, n+1):
        if i % 2 != 0:
            temp.append('수')
        else:
            temp.append('박')
    
    answer = ''.join(temp)
    
    return answer

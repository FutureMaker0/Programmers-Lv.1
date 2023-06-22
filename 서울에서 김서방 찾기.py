def solution(seoul):
    answer = ''
    
    for name in seoul:
        if name == 'Kim':
            answer = f"김서방은 {seoul.index(name)}에 있다"
    
    return answer

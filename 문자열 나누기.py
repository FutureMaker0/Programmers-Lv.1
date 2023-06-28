def solution(s):
    answer = 0
    same = 0
    diff = 0
    
    for elem in s:
        
        if same == diff:
            answer += 1
            head = elem
            
        if elem == head:
            same += 1
        else:
            diff += 1
    
    return answer

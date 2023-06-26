def solution(numbers):
    answer = -1
    temp = []
    
    for i in range(10):
        if i in numbers:
            continue
        temp.append(i)
    
    answer = sum(temp)
    
    return answer

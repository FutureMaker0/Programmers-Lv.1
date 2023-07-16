def solution(left, right):
    answer = 0
    temp = []
    temp2 = [[]]
    
    for num in range(left, right+1):
        for i in range(1, num+1):
            if num % i == 0:
                temp.append(i)
        print(temp)
        
        if len(temp) % 2 == 0:
            answer += num
        else:
            answer -= num
        
        temp = []
                
    return answer

def solution(arr, divisor):
    answer = []
    
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    
    # print(answer)
    
    if not answer:
        answer.append(-1)
        return answer
    else:
        answer.sort()
        return answer


def solution(food):
    answer = ''
    
    # food = list(map(str, food))
    
    for elem in enumerate(food):
        # print(elem, elem[1])
        for _ in range(1, (elem[1]//2)+1):
            answer += str(elem[0])
        # print(answer)
    
    return answer + '0' + answer[::-1]

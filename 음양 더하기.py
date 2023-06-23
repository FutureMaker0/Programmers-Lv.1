def solution(absolutes, signs):
    answer = 0
    
    result = zip(absolutes, signs)
    # print(list(result))
    
    for case in list(result):
        if case[1] == False:
            answer += (case[0] * (-1))
        else:
            answer += case[0]
    
    return answer

def solution(array, commands):
    answer = []
    result = []
    
    for case in commands:
        answer = array[case[0]-1:case[1]]
        
        answer.sort()
        result.append(answer[case[2] - 1])
    
    return result

def solution(s):
    answer = ''
    
    for word in s.split(' '):
        for elem in enumerate(word):
            # print(elem)
            if elem[0] % 2 == 0 or elem[0] == 0:
                answer += elem[1].upper()
            else:
                answer += elem[1].lower()
        answer += ' '
    
    answer = answer[0:-1]
        
    return answer

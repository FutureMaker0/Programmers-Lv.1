def solution(s, n):
    answer = ''
    
    for elem in s:
        if elem == ' ':
            answer += ' '
        else:
            if (ord(elem) <= 90 and ord(elem)+n > 90) or ord(elem) <= 122 and ord(elem)+n > 122:
                answer += chr(ord(elem) - (26 - n))
            else:
                answer += chr(ord(elem) + n)
        
    return answer


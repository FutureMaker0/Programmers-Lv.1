def solution(n):
    answer = []
    answer2 = 0

    n = str(n)
    for i in n:
        answer.append(i)
    
    answer.sort(reverse=True)
    answer = ''.join(answer)
    answer2 = int(answer)
    
    return answer2

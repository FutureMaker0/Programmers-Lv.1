from itertools import combinations

def solution(numbers):
    answer = []
    
    for i in combinations(numbers, 2):
        # print(i[0] + i[1])
        plus = i[0] + i[1]
        if plus not in answer:
            answer.append(plus)
    print(answer)
    answer.sort()
    
    return answer

from itertools import combinations

def solution(number):
    answer = 0
    cases = list(combinations(number, 3))
    
    for case in cases:
        # print(case, sum(case))
        if sum(case) == 0:
            answer += 1    
    
    return answer

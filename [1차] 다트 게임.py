# 기본적이지만 생각을 요하는 문제.
# 리스트 슬라이싱의 개념에 대해 정확한 이해 필요.
# list0 = [1]
# print(list0[-2:])
# = 에러 안남.

# list0 = [1, 2, 3, 4, 5]
# list[-2:0] = [4, 5] 
# 등등

def solution(dartResult):
    '''
    scores = []
    dict0 = {'S': 1, 'D': 2, 'T': 3}
    start_idx = 0

    # S = **1, D = **2, T = **3
    # *: 해당점수/앞전 점수 2배, 앞전 점수가 없을때는 본인만 2배
    # #: 해당 점수 마이너스
    
    for i in range(len(dartResult)):
        oper = dartResult[i]
        # print(oper)
        
        if oper in dict0:
            scores.append(int(dartResult[start_idx:i]) ** dict0[oper])
        elif oper == '*':
            scores[-2:] = [x*2 for x in scores[-2:]]
        elif oper == '#':
            scores[-1] = scores[-1] * (-1)
        else:
            continue
            
        if oper.isdigit() == False:
            start_idx = i + 1
        
    return sum(scores)
    '''
    
    answer = 0
    scores= []
    dict0 = {'S': 1, 'D': 2, 'T': 3}
    start_idx = 0
    
    for i in range(len(dartResult)):
        oper = dartResult[i]
        
        if oper in dict0:
            scores.append(int(dartResult[start_idx:i]) ** dict0[oper])
        elif oper == '*':
            scores[-2:] = [x*2 for x in scores[-2:]]
        elif oper == '#':
            scores[-1] *= -1
        
        if not oper.isnumeric():
            start_idx = i + 1
        
    return sum(scores)

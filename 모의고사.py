# 완전탐색 문제

def solution(answers):
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    # 고정된 규칙으로 답을 찍었으므로 모드 연산 활용
    # 2번 학생 기준 총 문제가 10개라고 하면, 2 1 2 3 2 4 2 5 2 1 까지 찍는 것.
    # 10번째 찍은 답은, stu2[9 % 8] = stu2[1] = 1이 되는 것.
    # 별거 아닌 것처럼 풀이되어 있으나 굉장히 생각해내기 어려운 개념으로 보임. 숙지.
    for idx, answer in enumerate(answers):
        # print(idx, answer)
        if answer == stu1[idx % len(stu1)]:
            score[0] += 1
        if answer == stu2[idx % len(stu2)]:
            score[1] += 1
        if answer == stu3[idx % len(stu3)]:
            score[2] += 1
    # print(score)
            
    for idx, elem in enumerate(score):
        if elem == max(score):
            # print(max(score))
            result.append(idx + 1)
        # print(result)
    return result
    
    
    '''
    런타임 에러
    
    answer = []
    cases = [[1, 2, 3, 4, 5], 
             [2, 1, 2, 3, 2, 4, 2, 5], 
             [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score_arr2 = []
    
    for i, case in enumerate(cases):
        case = case[:len(answers)]

        # print(case, answers)

        score_arr = []
        for k in range(len(answers)):
            if case[k] == answers[k]:
                score_arr.append(1)
                
        # print(len(score_arr), score_arr2)
        score_arr2.append(len(score_arr))
        
    # print(score_arr2)
    # score_arr2.sort(reverse=True)
    score_arr3 = sorted(score_arr2, key= lambda x: (x, score_arr2.index(x)), reverse=True)
    
    for m in enumerate(score_arr3):
        # print(m)
        if m[1] == 0:
            continue
        else:
            answer.append(m[0]+1)
    '''

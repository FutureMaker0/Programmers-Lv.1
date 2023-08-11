# 해시

def solution(participant, completion):
    answer = {}
    
    for i in participant:
        # print(i)
        # print(answer.get(i, 0))
        answer[i] = answer.get(i, 0) + 1 # 사실상 초기화 작업
        # print(answer.get(i, 0))
    
    for j in completion:
        answer[j] -= 1
    
    for k in answer:
        if answer[k]: return k


'''
# 해시 함수로 나온 값은 입력값이 똑같다면 나온 값은 무조건 똑같다.
def solution(participant, completion):
    result = 0
    answer = {}
    
    for p_person in participant:
        answer[hash(p_person)] = p_person
        result += hash(p_person)
    
    for c_person in completion:
        result -= hash(c_person)
        
    return answer[result] # 딕셔너리는 기본적으로 문자열 반환
'''

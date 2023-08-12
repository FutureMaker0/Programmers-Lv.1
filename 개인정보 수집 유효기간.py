def to_days(t):
    y, m, d = map(int, t.split('.'))
    return y*12*28 + m*28 + d

# 약관을 일단 해시로
def solution(today, terms, privacies):
    dict1 = {}
    answer = []
    today = to_days(today)
    print(today)

    # 우선 딕셔너리를 구성. 약관 종류별 일수를 value로 저장.
    for term in terms:
        # print(term.split(' ')[0], term.split(' ')[1])
        dict1[term.split(' ')[0]] = int(term.split(' ')[1]) * 28
    print(dict1)
    
    '''
    에러코드, 뭐가 다른지 이해가 안됨...
    for privacy in privacies:
        print(to_days(privacy[:-2]) + dict1[privacy[-1]], today)
        limit_date = to_days(privacy[:-2]) + dict1[privacy[-1]]
        
        if limit_date <= today:
            answer.append(privacies.index(privacy)+1)
    '''

    # 인덱스가 필요할 때는, .index() 보다는
    # enumerate 함수를 써서 추출된 idx 값을 활용하자.
    for i, privacy in enumerate(privacies, 1):
        print(to_days(privacy[:-2]) + dict1[privacy[-1]], today)
        limit_date = to_days(privacy[:-2]) + dict1[privacy[-1]]
        
        if limit_date <= today:
            answer.append(i)
    
    # print(answer)
    return answer
    

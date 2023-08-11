# 제한사항 조건을 모두 충족시켜야 한다.
# 런타임 에러라고 해서 무조건 시간복잡도 초과가 아니다.
# 제한사항 불만족 시에도 런타임 에러가 난다.

from collections import Counter

def solution(N, stages):
    answer = {}
    l = len(stages)
    
    s = Counter(stages)
    # print(s)
    # print(s[1], s[2], s[3], s[4], s[5])
    
    for i in range(1, N+1):
        if l and s[i]:
            fail_rate = s[i] / l
            answer[i] = fail_rate
            l -= s[i]
        else:
            answer[i] = 0
    # print(answer)
    
    sorted_dict = sorted(answer.items(), key=lambda x:x[1], reverse=True)
    # print(sorted_dict)
    
    return [elem[0] for elem in sorted_dict]
    

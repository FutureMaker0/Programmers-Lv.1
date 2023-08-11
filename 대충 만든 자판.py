# 3중 for문을 돌려도 된다고? - Lv.1까지만 허용, 이렇게 풀이하는 것 지양.
'''
def solution(keymap, targets):
    answer = [] # 최종 답
    
    for target in targets: # 일단 타겟이 되는걸 먼저 꺼낸다
        
        cnt = [] # 타겟의 각 문자를 입력하는데 필요한 키 누름 횟수 저장용
        for char in target: # 타겟에서 하나하나 빼서 대조할 준비를 한다
            
            idx = [] # 각 문자에 대해 key(각 행)에서 char의 인덱스를 추가하기 위함
             # 그러고 나면 idx 리스트에서 최솟값 선택을 통해 누른 횟수를 최소로 카운팅함
            for key in keymap: # 키맵이 어떻게 되있는지 확인을 위해 하나씩 뺀다
                
                if char in key:
                    idx.append(key.index(char)+1) # 키맵에 타겟문자가 잇으면 일단 인덱스 저장 (+1)
            
            if idx: # 일단 키맵에서 순서를 넣어놓은 상태에서, 뭐가 최소인지를 판별한다
                cnt.append(min(idx)) # 최솟값만 cnt 리스트로 다시 거른다
                
        print(cnt)
        if len(cnt) == len(target):
            answer.append(sum(cnt))
        else:
            answer.append(-1)
    
    return answer
'''

# 딕셔너리 해시를 이용한 시간복잡도 감축 풀이
def solution(keymap, targets):
    answer = []
    dict1 = {} # 키보드 왼쪽 가장자리에서 키보드의 각 문자까지의 최소 거리 저장용
    
    for key in keymap:
        for idx, char in enumerate(key, 1):
            # print(idx, char)
            if char in dict1:
                dict1[char] = min(idx, dict1[char])
            else:
                dict1[char] = idx
        # print(dict1)

    for target in targets:
        cnt = 0
        for elem in target:
            if elem in dict1:
                cnt += dict1[elem]
            else:
                cnt = -1
                break # 직속상위 for 반복문을 그대로 멈춘다. (for elem in target:)
        
        answer.append(cnt)

    return answer
    
    

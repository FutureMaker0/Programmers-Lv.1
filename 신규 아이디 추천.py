def solution(new_id):
    answer = ''
    allow_special = ['-', '_', '.']
    
    # 1단계
    new_id = new_id.lower()
    # print(new_id)
    
    # 2단계
    # while문을 사용하면 out of index range 에러에서 비교적 자유롭다
    i = 0
    while i < len(new_id):
        oper = new_id[i]
        # print(oper)
        if oper.isnumeric() or oper.islower() or oper in allow_special:
            i += 1
        else:
            # print(oper, 'this!')
            new_id = new_id.replace(oper, '')
    # print(new_id)
    
    # 3단계
    # print(new_id.count('.'))
    temp = ''
    prev_char = ''
    for char in new_id:
        if char == '.' and prev_char == '.':
            continue
        temp += char
        prev_char = char
    # print(temp)
    
    new_id = temp
    # print(new_id)
    
    # 4단계
    # 빈 문자열에서 슬라이싱을 통해 잘라내려고 하면 string out of range 에러 발생
    # 문자열이 있는지 먼저 확인 하고 조건검증 필요
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
        # print(new_id)
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
        # print(new_id)
        
    # 5단계
    if not new_id:
        new_id += 'a'
    # print(new_id)
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    # print(new_id)
    
    # 7단계
    if len(new_id) <= 2:
        for i in range(3-len(new_id)):
            new_id += new_id[-1]
    # print(new_id)

    return new_id

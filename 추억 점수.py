def solution(name, yearning, photo):
    answer = []
    result = list(zip(name, yearning))
    print(result)
    
    cnt = 0
    for case in photo:
        for name in case:
            for zip_case in result:
                if name == zip_case[0]:
                    cnt += zip_case[1]
        # print(cnt)
        answer.append(cnt)
        cnt = 0
    
    return answer

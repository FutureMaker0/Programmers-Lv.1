def solution(d, budget):
    answer = 0
    cnt = 0
    
    d.sort()
    # print(d)
    for num in d:
        answer += num
        if answer <= budget:
            cnt += 1
        else:
            break
    
    return cnt

def solution(s):
    answer = []
    my_dict = {}
    
    for idx, elem in enumerate(list(s)):
        # print(idx, word)
        if elem not in my_dict:
            answer.append(-1)
            my_dict[elem] = idx
            
        else:
            # 핵심라인
            answer.append(idx - my_dict[elem]) 
            # a: 3 - 1 = 2, n: 4 - 2 = 2, a: 5 - 3 = 2
            
            my_dict[elem] = idx
            # a = 3, n = 4
            
    return answer


def solution(lottos, win_nums):
    unknown = 0
    known = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    for num in lottos:
        if num == 0:
            unknown += 1
        elif num in win_nums:
            known += 1
    print(unknown, known)
    
    return [rank[unknown+known], rank[known]]
            
    

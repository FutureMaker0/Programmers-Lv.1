# 반복문을 통한 스왑 시 시간초과 발생
# 딕셔너리를 통한 시간 복잡도 축소 필수
def solution(players, callings):  
    dict0 = {}
    for idx, player in enumerate(players):
        # print(idx, player)
        dict0.update({player: idx})
    # print(dict0)
    
    for calling in callings:
        recent_rank = dict0[calling]
        # print(recent_rank)
        dict0[calling] -= 1
        dict0[players[recent_rank-1]] += 1
        # print(dict0)
        
        players[recent_rank-1], players[recent_rank] = players[recent_rank], players[recent_rank-1] 

    return players
    

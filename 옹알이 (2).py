def solution(babbling):
    cansay = ['aya', 'ye', 'woo', 'ma']
    answer = 0
	
    for babble in babbling:
        # print(babble)
        for can in cansay:
            if can*2 in babble:
                break
            babble = babble.replace(can, ' ')
            print(babble)
    
        # if not babble.strip():
        if babble.isspace(): # 공백으로만 이루어져 있을 때, 
            answer += 1
    
    return answer

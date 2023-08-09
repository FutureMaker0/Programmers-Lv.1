# heap은 원소들이 자동정렬 되는 것을 이용한다.
# 정렬 과정을 거칠 필요가 없기 떄문에 시간 복잡도가 굉장히 감소한다.

'''
import heapq

def solution(k, score):
    h = []
    result_h = []
    
    for num in score:
        heapq.heappush(h, num)
        # print(h)
        
        if len(h) > k:
            heapq.heappop(h)
            # print(h)
        
        result_h.append(h[0])
    
    return result_h
'''

import heapq

def solution(k, score):
    h = []
    answer_h = []

    for elem in score:
        heapq.heappush(h, elem)
        
        if len(h) > k:
            heapq.heappop(h)
            
        answer_h.append(h[0])
    
    return answer_h

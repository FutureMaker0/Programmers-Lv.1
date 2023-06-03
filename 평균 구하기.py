def solution(arr):
    answer = 0
    total = 0
    
    for num in arr:
        total += num
    answer = total / len(arr)
    
    return answer

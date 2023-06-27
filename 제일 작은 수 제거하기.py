def solution(arr):
    # answer = []
    min_value = min(arr)
    
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min_value)
    
    return arr


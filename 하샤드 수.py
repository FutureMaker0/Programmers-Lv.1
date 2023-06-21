def solution(x):
    answer = True
    plus = 0
    
    for i in str(x):
        plus += int(i)
    
    if x % plus == 0:
        return True
    return False


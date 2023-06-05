import math

def solution(n):
    answer = 0
    value = math.sqrt(n)
    
    if value == int(value):
        return (value+1) ** 2
    return -1

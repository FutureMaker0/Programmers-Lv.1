import math

def solution(n, m):
    answer = []
    gcd = math.gcd(n,m)
    lcm = 0
    
    if m % n == 0:
        lcm = m
    else:
        lcm = (m*n)/gcd
    
    answer = [gcd, lcm]
    
    return answer

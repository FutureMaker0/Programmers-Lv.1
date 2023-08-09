# 재귀?로 하고싶다..
'''
def solution(a, b, n):
    answer = 0
    
    while n >= a:
        new = (n // a) * b
        answer += new
        rest = n % a
    
        n = new + rest     
        
    return answer
        
'''

'''
6 
8 2
4 1
1
'''
import sys
sys.setrecursionlimit(10000)

def solution(a, b, n):
    if n < a:
        return 0
    
    new = (n // a) * b
    rest = n % a
    
    return new + solution(a, b, new + rest)




'''
def collatz(n, answer):
    if n == 1:
        return answer
    if answer == 500:
        return -1
    
    if n%2==0:
        return collatz(n//2, answer+1)
    else:
        return collatz(n*3+1, answer+1)
    
def solution(n):
    return collatz(n, 0)
'''



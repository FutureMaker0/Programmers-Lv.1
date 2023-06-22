# 이 문제는 무식 구현이 아닌 재귀 문제다.
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

# 모든 재귀는 반복문을 통한 작업으로 변경할 수 있다.
def collatz(n):
    if n==1: return 0
    for i in range(500):
        n=n/2 if n%2==0 else n*3+1 # 축약 조건문을 쓸 땐, n/=2가 안된다.
        if n==1: return i+1
    return -1

def solution(n):
    return collatz(n)
    
    
    

# 복잡한 문제는 아래와 같은 코드로는 절대 통과할 수 없다.
    '''
    answer = 0
    
    if n == 1:
        return 0
    
    if n % 2 == 0:
        while n > 1:
    
            n //= 2
            answer += 1
            
            if n % 2 == 0:
                n //= 2
                answer += 1
            else:
                n = (n*3) + 1
                answer += 1
                
        if answer >= 500: return -1
        
    else:
        while n > 1: 
            n = (n*3) + 1
            answer += 1

            if n % 2 == 0:
                n //= 2
                answer += 1
            else:
                n = (n*3) + 1
                answer += 1
                
                if answer >= 500: return -1
    '''

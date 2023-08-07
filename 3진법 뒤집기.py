def solution(n):
    answer = ''
    
    while n>0:
        answer += str(n%3)
        n //= 3
    
    decimal = int(answer, 3)
    
    return decimal

'''
45 3 - 15 0
15 3 - 5 0
5 3 - 1 2
1 3 - 1

125 3 - 41 2
41 3 - 13 2
13 3 - 4 1
4 3 - 1 1
1 3 - 0 1
11122 -> 22111 = 7

'''



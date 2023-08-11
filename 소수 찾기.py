def solution(n):
    answer = 0
    
    '''
    temp = []
    temp2 = []
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                temp.append(j)
        # print(temp)
        temp2.append(temp)
        temp = []
    # print(temp2)
    
    for elem in temp2:
        if len(elem) == 2:
            answer += 1
    '''
    
    # 에라토스테네스의 체 - 효율적인 소수판별 알고리즘
    primes = []
    is_prime = [True] * (n+1)
    
    for num in range(2, n+1):
        if is_prime[num] == True:
            primes.append(num)
            for multiple in range(num*2, n+1, num):
                is_prime[multiple] = False
    
    '''
    2 - 4, 6, 8, 10 제외
    3 - 6, 9 제외
    4 - 2에서 제외되서 미확인
    5 - 10 제외
    6 - 2에서 제외되서 미확인
    7 - 14 제외
    8 - 2에서 제외되서 미확인
    9 - 3에서 제외되서 미확인
    10 - 2에서 제외되서 미확인
    
    결국 2, 3, 5, 7 만 남는다.
    '''
    
    return len(primes)


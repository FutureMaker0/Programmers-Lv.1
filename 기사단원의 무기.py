# 결국엔 효율성을 따져야 한다.
# 입력 100,000만개 인데 10초 리밋이므로,
# 빅오 엔 제곱 미만까지 허용되는 것이다. 그러므로 이중포문을 쓰게되면 시간초과.

'''
N의 약수를 구할 때 1부터 N까지 순회는 그만.
1. 소인수분해를 이용
-. N이 24일 때, 이를 소인수 분해하면 2³ * 3¹이며 각 지수에 1을 더한 뒤 곱하면 
   (3 + 1) * (1 + 1) = 8로 약수의 개수를 구할 수 있다.

2. N의 제곱근으로 범위를 좁혀 탐색
-. N이 24일 때, 제곱근은 4.9
-. 정수 제곱근 4까지만 탐색을 해도,
    1 * 24 2개
    2 * 12 2개
    3 * 8  2개
    4 * 6  2개
    이후는 거꾸로 하는 과정이므로 총 8개 1, 2, 3, 4, 6, 8, 12, 24

    N%i==0인 경우, 1, 2, 3, 4 --> 약수의 갯수를 2개 카운트
    16과 같이 제곱수인 경우, N/i==i인 경우 같은 수 제곱이므로 2개 카운트에서 1개 빼준다.

'''


# 37.0점 짜리 코드 - 54.0에서 더 하락...

'''
import math

def solution(number, limit, power):
    answer = 0
    temp = []
    
    # 2번 방식 - 제곱근으로 좁혀서 탐색
    for i in range(1, number+1):
#         print(' ')
#         print(f'i값: {i}')
#         print(f'이전 answer값: {answer}')
        
        for j in range(1, int(math.sqrt(i))+1):
            # print(f'j값: {j}, int(math.sqrt(i))+1 값: {int(math.sqrt(i))+1}')
            
            if i%j == 0:
                answer += 2
                # print(answer)
                if i/j == j:
                    answer -= 1
                    # print(answer)
        # print(answer)
        temp.append(answer)
    # print(temp)
            
    difference = [temp[i+1] - temp[i] for i in range(len(temp)-1)]
    filtered_diff = list(filter(lambda x: x>limit, difference))
    
    return temp[-1] - (len(filtered_diff) * 2)
'''

# for 문으로 약수 찾을 때, 제곱근 까지만 탐색해도 왠만한 시간초과는 해결된다.
# 1. 제곱근까지 범위를 줄여서
# 2. 제곱수인지 아닌지에 따라 2개 카운트할지, 1개 카운트할지 결정해서 각 숫자별 약수갯수 도출
def solution(number, limit, power):
    answer = 0
    temp = []
    
    for i in range(1, number+1):
        cnt = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                if j*j == i:
                    cnt += 1
                else:
                    cnt += 2
        temp.append(cnt)
    # print(temp)
    
    for elem in temp:
        if elem > limit:
            answer += power
        else:
            answer += elem
    
    return answer
    

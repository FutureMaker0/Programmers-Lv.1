import math
from itertools import combinations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
def solution(nums):
    combi_list = combinations(nums, 3)
    
    answer = 0
    for elem in combi_list:
        if is_prime(sum(elem)):
            answer += 1
    
    return answer
    

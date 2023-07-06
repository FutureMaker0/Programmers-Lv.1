# 이중 for문, for-while 반복문 중첩은 애초에 불가.
# 해시 활용.

from string import ascii_lowercase
# from string import ascii_uppercase
# set은 정렬이 안되고 랜덤이다.

def solution(s, skip, index):
    answer = ''
    
    # print(ascii_lowercase)
    a_to_z = sorted(set(ascii_lowercase) - set(skip))
    
    # alpha_dict = {alpha: idx for idx, alpha in enumerate(a_to_z)}
    alpha_dict = {}
    for idx, alpha in enumerate(a_to_z, 1):
        alpha_dict[alpha] = idx
    
    for elem in s:
        answer += a_to_z[(alpha_dict[elem] + index) % len(alpha_dict) - 1]
    
    return answer
    

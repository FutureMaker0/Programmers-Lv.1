# 햄버거 문제는 스택
# 마지막 네개가 1231이면 카운트 하나 올리고, 1231 지운다.
# 빠진 상태에서 elem 끝날때까지 계속 반복.
# 1: 빵, 2: 야채, 3: 고기
# 1231이 붙어있는게 빠지고 다시 1231이 나와야만
# 카운팅이 가능하다.

def solution(ingredient):
    stack = []
    burger_cnt = 0
    
    for elem in ingredient:
        stack.append(elem)
        if stack[-4:] == [1, 2, 3, 1]:
            burger_cnt += 1
            for _ in range(4):
                stack.pop()
            
    return burger_cnt

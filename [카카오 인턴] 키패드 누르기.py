# 구현 난이도 중

def solution(numbers, hand):
    answer = ''
    
    # 키패드 숫자 종류 및 기준점에서의 거리를 딕셔너리로, 리스트 원소가 int로 '' 필요없음.
    left = {1: 3, 4: 2, 7: 1}
    right = {3: 3, 6: 2, 9: 1}
    center = {2: 3, 5: 2, 8: 1, 0: 0}
    
    # 현재 왼쪽, 오른쪽 손가락의 위치
    left_pos = (0, 0)
    right_pos = (2, 0)
    
    for number in numbers:
        if number in left:
            answer += 'L'
            left_pos = (0, left[number])
        elif number in right:
            answer += 'R'
            right_pos = (2, right[number])
        else:
            # 현재 포지션에서 센터 number까지의 거리 계산 - (가로) + abs(세로)
            # 거리계산까지 해놓으면 거의 끝났다.
            left_dist = (1 - left_pos[0]) + abs(center[number]-left_pos[1])
            right_dist = (right_pos[0] - 1) + abs(center[number]-right_pos[1])
        
            if left_dist < right_dist:
                answer += 'L'
                left_pos = (1, center[number])
            elif left_dist > right_dist:
                answer += 'R'
                right_pos = (1, center[number])
            else: # 두 손가락의 거리가 같을 때,
                if hand == 'left':
                    answer += 'L'
                    left_pos = (1, center[number])
                else:
                    answer += 'R'
                    right_pos = (1, center[number])
    
    return answer
    

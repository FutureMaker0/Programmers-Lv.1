'''
move
1 5 3 5 1 2 1 4

0 0 0 0 0
0 0 1 0 3
0 2 5 0 1
4 2 4 4 2
3 5 1 3 1

4 3 1 1 3 2 4 -> 4 3 3 2 4 -> 4 2 4 = 터진인형 4개

'''

def solution(board, moves):
    answer = 0
    box = []
    
    # 인형 집어올리기 및 스택에 담기 - 중복제거 전
    for move in moves:
        move -= 1
        for row in board:
            # print(row[move])
            if row[move]:
                box.append(row[move])
                row[move] = 0
                break
    # print(box)
    
    # 중복여부 확인 후 터진 인형갯수 카운트
    i = 0
    while i < len(box) - 1:
        if box[i] == box[i + 1]:
            box.pop(i)
            box.pop(i)
            answer += 2
            i = max(0, i - 1)
        else:
            i += 1
    
    return answer

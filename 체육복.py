'''
그리디 알고리즘은, 그냥 앞에서부터 무식하게 돌려가면서 비교해서 원하는 값을
얻어내는 것이다.
'''

def solution(n, lost, reserve):
    # 체육복 여벌을 가져온 학생이 도난 당한 경우 처리
    # 여벌을 가져온 학생이 도난을 당하면 더 이상 여벌이 있지 않기 때문에 reserve에서 제외
    real_reserve = set(reserve) - set(lost)
    print(real_reserve)

    # 체육복을 도난당한 학생이 여벌이 있는 경우 처리
    # 여벌이 있는 학생은 도난을 당해도 하나가 남기 때문에 lost 리스트에서 제외
    real_lost = set(lost) - set(reserve)
    print(real_lost)
    
    # 도난당한 학생 기준으로 앞, 뒤 번호 학생에게 체육복을 빌리는 과정
    # if, elif 중 하나만 만족하면 거기서 바로 다음 student로 넘어가고
    # else에 도달했을 때만 n-1을 해준다.
    for student in real_lost:
        if (student - 1) in real_reserve:
            real_reserve.remove(student - 1)
        elif (student + 1) in real_reserve:
            real_reserve.remove(student + 1)
        else:
            n -= 1  # 체육복을 빌리지 못한 경우
    
    answer = n
    return answer


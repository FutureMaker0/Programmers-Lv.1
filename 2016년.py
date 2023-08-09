def solution(a, b):
    # 12월 31일 목요일
    # 1월 1일 금요일
    # 2월 1일 월요일
    
    answer = ''
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    total_days = sum(months[:a-1]) + b - 1
    yoil_index = total_days % 7
    
    yoil = days[yoil_index]
    answer += yoil
    
    return answer

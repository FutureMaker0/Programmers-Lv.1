def solution(s):
    # answer = True
    
    cnt_p = 0
    cnt_y = 0
    
    if 'p' not in s and 'P' not in s and 'y' not in s and 'Y' not in s:
        return True
    
    else:
        for i in s:
            if i == 'p' or i == 'P':
                cnt_p += 1
            elif i == 'y' or i == 'Y':
                cnt_y += 1

        if cnt_p == cnt_y:
            return True
        return False
    

def solution(s):
    answer = True
    
    if len(s)==4 and s.isdigit() == False:
        return False
    elif len(s)==4 and s.isdigit() == True:
        return True
    elif len(s)==6 and s.isdigit() == False:
        return False
    elif len(s)==6 and s.isdigit() == True:
        return True
    else:
        return False

    # return answer

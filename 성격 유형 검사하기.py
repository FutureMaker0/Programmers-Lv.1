dict1 = {
    'R': 0,
    'T': 0,
    'C': 0,
    'F': 0,
    'J': 0,
    'M': 0,
    'A': 0,
    'N': 0,
}

dict2 = {
    '1': 3,
    '2': 2,
    '3': 1,
    '4': 0,
    '5': 1,
    '6': 2,
    '7': 3,
}

def solution(survey, choices):
    idx = 4
    new_survey = list(zip(survey, choices))
    # print(new_survey)
    
    answer = ''
    
    for elem in new_survey:
        # print(elem[0][0], elem[0][1], elem[1])
        if elem[1] < idx:
            dict1[elem[0][0]] += dict2[str(elem[1])]
            # dict1[elem[0][0]] += 1
        else:
            dict1[elem[0][1]] += dict2[str(elem[1])]
            # dict1[elem[0][0]] += 1
    print(dict1)

    for typ1, typ2 in ('RT', 'CF', 'JM', 'AN'):
        
        answer += typ1 if dict1[typ1] >= dict1[typ2] else typ2 # for문 축약
        
        '''
        if dict1[typ1] >= dict1[typ2]:
            answer += typ1
        else:
            answer += typ2
        '''

    return answer

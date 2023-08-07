# binary = format(9, f'0{5}b')
    # print(binary)
    
def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    
    for num1 in arr1:
        result1 = format(num1, f'0{n}b')
        map1.append(result1)
    
    for num2 in arr2:
        result2 = format(num2, f'0{n}b')
        map2.append(result2)
    
    for i in range(n):
        answer2 = []
        for j in range(n):
            if int(map1[i][j]) | int(map2[i][j]) == 1:
                answer2.append('#')
            else:
                answer2.append(' ')
        answer.append(answer2)
    
    result = ''
    answer3 = []
    for case in answer:
        for k in case:
            result += k
        answer3.append(result)
        result = ''
        
    return answer3


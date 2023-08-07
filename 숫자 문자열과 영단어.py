nums = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

'''
def solution(s):
    for key, value in nums.items():
        # print(key, value)
        s = s.replace(key, value)
    
    return int(s)
'''

def solution(s):
    answer = ''
    buffer = ''
    
    for char in s:
        if char.isnumeric():
            answer += char
        else:
            buffer += char
            
            if len(buffer) >= 3 and buffer in nums:
                answer += nums[buffer]
                buffer = ''
        
    return int(answer)
    

# difficult

def solution(park, routes):
    # 전체 park 크기 구함
    w, h = len(park), len(park[0])
    
    news = {'N': [0, -1], 'E': [1, 0], 'W': [-1, 0], 'S': [0, 1]}
    
    # 초기 좌표 구함
    for i, v in enumerate(park):
        if 'S' in v:
            y, x = i, v.index('S')
    
    for route in routes:
        direction, steps = route.split(' ')
        steps = int(steps)
        
        pos_x, pos_y = news[direction]
        
        if not(x+(pos_x*steps) in range(0, h) and y+(pos_y*steps) in range(0, w)):
            continue
        
        else:
            block = False
            for step in range(1, steps+1):
                if park[y+(pos_y*step)][x+(pos_x*step)] == 'X':
                    block = True
                    break
            
        if not block:
            x += pos_x * steps
            y += pos_y * steps
    
    return [y, x]
    

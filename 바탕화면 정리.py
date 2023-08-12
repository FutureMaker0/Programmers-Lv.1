def solution(wallpaper):
    x = []
    y = []
    
    for i in range(len(wallpaper)):
        # print(wallpaper[i])
        for j in range(len(wallpaper[i])):
            print(wallpaper[i][j], end='')
            
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
    
    return [min(x), min(y), max(x)+1, max(y)+1]

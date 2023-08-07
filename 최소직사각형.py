def solution(sizes):
    x = []
    y = []
    
    for size in sizes:
        if size[0] < size[1]:
            x.append(size[1])
            y.append(size[0])
        else:
            x.append(size[0])
            y.append(size[1])
        
    return max(x) * max(y)
    

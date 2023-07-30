def solution(price, money, count):
    answer = 0
    price_per_time = []

    for i in range(1, count+1):
        price_per_time.append(price * i)
        
    if sum(price_per_time) <= money:
        return 0
    else:
        return sum(price_per_time) - money
    


'''
price: 3
money: 20
count: 1 2 3 4
new  : 3 6 9 12 (price*count)
answer = sum(new) - money
'''


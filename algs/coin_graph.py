#Returns the least number of coins needed to reach a number
#Applying and utilizing Dynamic Programming Principles

coins =[1,2,5,10,20,50,100,200,500]
pairs={}
def coin_to(num):
    if num in coins:
        x=1
        return x
    elif num in pairs.keys():
        x = pairs[num]
        return x
    else:
        x= 1+min([coin_to(num-coin) for coin in coins if coin <num ])
        pairs[num]=x
        return x

print (coin_to(501))
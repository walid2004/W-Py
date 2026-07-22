#Returns the least number of coins needed to reach a number
#Applying and utilizing Dynamic Programming Principles

coins =[1,2,5,10,20,50,100,200,500]
def coin_to(num):
    if num in coins:
        x=1
        return x
    else: 
        x= 1+min([coin_to(num-coin) for coin in coins if coin <num ])
        return x

print (coin_to(33))
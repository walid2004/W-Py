#Returns the least number of coins needed to reach a number
#Applying and utilizing Dynamic Programming Principles
zz=None
coins =[5,10,20,50,100,200,500]
pairs={'solution':set([])}
def coin_to(num,cz=0):
    global zz
    if num in coins:
        x=1
        pairs['solution'].add(num)
        return x
    elif num in pairs.keys():
        x = pairs[num]
        return x
    else:
        z=[(coin_to(num-coin),num,num-coin,coin) for coin in coins if coin <num ]
        y=min(reversed(z), key = lambda item: item[0]) #y = min(reversed(z), key=lambda item: item[0])
        x= 1+min(z)[0]
        zz=y
        print(zz)
        pairs[num]=x
        return x

print (coin_to(75))

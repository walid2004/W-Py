#Returns the least number of coins needed to reach a number
#Applying and utilizing Dynamic Programming Principles
zz=None
coins =[1,2,5,10,20,50,100,200,500]
pairs={'solution':[], 'xx':{}}

def coin_to(num,flag= True):
    global zz
    if num in coins:
        x=1
        print((1,num,0,num))
        pairs['xx'][num]=(1,num,0,num)
        return x
    elif num in pairs.keys():
        x = pairs[num]
        return x
    else:
        z=[(coin_to(num-coin,flag=False),num,num-coin,coin) for coin in coins if coin <num ]
        y=min(reversed(z), key = lambda item: item[0]) #y = min(reversed(z), key=lambda item: item[0])
        x= 1+min(z)[0]
        zz=y
        pairs['xx'][zz[1]]=zz
        print(zz)
        pairs[num]=x
        if flag:
            return x, pair_parser(num)
        return x
    
def pair_parser(num):
    xl = pairs['xx']
    while num >0:
        focus = xl[num]
        pairs['solution'].append(focus[3])
        num-=focus[3]
    return pairs['solution']
input =67
print (coin_to(input))
#starting a new arch
import math
class wpy:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
    
    def __init__(self):
        self.name= 'wpy'
        self.version = '0.0'

    def unique_Values(self, dataset):
        unique={}
        for i in dataset:
            if i in unique.values():
                unique[i]+=1
            else:
                unique[i]=1
        return(unique, len(unique))

    def entropy(self, dataset):
        k= self.unique_Values(dataset)
        n= len(dataset)
        entropy_sum =0
        for value in k.keys:
            probability = k[value]/n
            log = math.log(2,probability)
            entropy_sum -= probability*log
        return entropy_sum
    



        
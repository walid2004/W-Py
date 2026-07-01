#starting a new arch
class wpy:
    def __init__(self):
        self.name= 'wpy'
        self.version = '0.0'

    def unique_Values(self, dataset):
        unique={}
        for i in dataset:
            if i in unique.values:
                unique[i]+=1
            else:
                unique[i]=1
        return(unique, len(unique))

    def entropy(self, dataset):
        k= self.unique_Values(dataset)
        n= len(dataset)
        for value in k.keys:
            probability = k[value]/n
            

        
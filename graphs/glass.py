#solving the glass pouring problem using the shortest path graph algorithm

class Glass:
    self.level = 0
    def __init__(self, capacity):
        self.capacity = capacity
        self.level =0

    def emptying(self):
        self.level=0

    def fulling(self):
        self.level= self.capacity
    
    def transferring(self,other_glass):
        self.level = other_glass.capacity - other_glass.level
        



def glass_problem(cap_1,cap_2,start_1,start_2, goal_1,goal_2):
    n=0
    while (start_1 and start_2)!=(goal_1,goal_2):

        pass




    return n
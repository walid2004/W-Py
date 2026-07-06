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
    
    def free(self):
        return (self.capacity - self.level)
    
    def transferring(self,other_glass):
        if other_glass.free()>= self.level:
            other_glass.level +=self.level
            self.level = 0
        else:
            self.level-= other_glass.free()
            other_glass.level = other_glass.capacity
        



def glass_problem(cap_1,cap_2,start_1,start_2, goal_1,goal_2):
    glass_a = Glass(cap_1)
    glass_b = Glass(cap_2)
    n=0
    frontier=[]
    while (start_1 and start_2)!=(goal_1,goal_2):
        
        pass




    return len(frontier)
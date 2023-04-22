import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        for key in kwargs:
            numbers=kwargs[key]
            for x in range(numbers):
                self.contents.append(key)
    
    def draw(self,number):
        MaxBalls=len(self.contents)
        removed=[]
        if number>MaxBalls:
            return self.contents
        else:
            for x in range(number):
                ChoosenNumber=random.randrange(len(self.contents))
                ChoosenBall=self.contents[ChoosenNumber]
                removed.append(ChoosenBall)
                del self.contents[ChoosenNumber]
        return removed



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    Count=0
    for exp_no in range(num_experiments):
        hat_copy=copy.deepcopy(hat)
        excepted_copy=copy.deepcopy(expected_balls)
        ballsDrawn=hat_copy.draw(num_balls_drawn)
        for balls in ballsDrawn:
            if (balls in excepted_copy):
                excepted_copy[balls]-=1
        if (all(values<=0 for values in excepted_copy.values())):
            Count+=1
        
    return Count/num_experiments
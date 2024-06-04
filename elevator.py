import queue
from settings import *
import time

class Elevator:
    def __init__(self,number_elv, x, y):
        self.current_floor = 0
        self.target_floor = None                                                   #start
        self.queue =[]             #build arry
        self.total = 0
        self.moving = False
        self.x_position = x
        self.y_position = y
        self.start_y = y
        self.start_rest = None # start rest time
        #self.final_d = None 


    '''def final_d(self):
        if not self.queue:
            return self.current_floor
        return self.queue[-1]'''
    
    def time_to_be_free(self):
        if not self.queue:        #if is empty
            self.total = 0
        else:

            floor = self.current_floor
            for next_floor in self.queue:
                self.total += abs(floor - next_floor) * time_for_floor + DELAY_TIME
                floor = next_floor

        return self.total
    
    def total_time(self,new_floor):
       
        total_g = self.total +abs(self.queue[-1] - new_floor) * 0.5
       
        return total_g
        
    def exit_time(self):
        pass
    def time(self):
        pass
    

    def rest_over(self):   #if 2second over 
        current_time = time.time()
        if current_time - self.start_rest >= 2 :
            self.moving == True


    def update(self):
        current_time = time.time()
    #all time y now were she is and the time 
        if self.moving == False:
            if len(self.queue) != 0: # elv is resting
                if current_time - self.start_rest >= 2:
                    pass
                    


                
            else:                   #if queue not empty
                pass
        else:                         #if moving = true 
            pass


    
        
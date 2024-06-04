from elevator import Elevator
from floor import Floor
from settings import *

class building:
    def __init__(self):
        self.list_elevators = []
        self.list_floors = []

    def make_elevators(self):
        x = FLOOR_WIDTH + ELV_GAP
        y = SCREEN_HEIGHT - ELV_HEIGHT - GAP_HEIGHT
        for number in range(NUM_ELEVATORS):
           self.list_elevators.append(Elevator(number , x , y))
           x += ELV_GAP
           
             


    def make_floors(self):
        x = 0
        y = SCREEN_HEIGHT - GAP_HEIGHT - FLOOR_HEIGHT
        for number in range(NUM_FLOORS):
            self.list_floors.append(Floor(number, x ,y))
            y -= (GAP_HEIGHT + FLOOR_HEIGHT)

    def get_min_elv(self, floor_num):
        pass

    


    
    def get_min_ele(self, floor_num):
        
        min_elv = float('inf')
        for elevator in self.list_elevators:
            if elevator.total_time(elevator) < min_elv:
                min_elv = elevator

        return min_elv

        
        pass
        
        
        pass
        floor = self.floors[floor_num]
        floor.elevator_called()


Elevator.final_d(2)

'''floors =10
new_floors = []
for i  in range(floors):
    new_floors.append(i)

floors = new_floors
print (floors)''' 
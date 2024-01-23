from math import *
from random import *

places = ["City A", "City B", "Town C", "Village D", "Metropolis E"]

class TimeTravel:
    def __init__(self, curr_time):
        self.curr_time = curr_time
        self.future_time = curr_time


    def next_year(self):
        self.portal = choice(places)
        self.future_time += self.portal.__len__() * e * (((1<<1<<1<<1|1<<0))|(0 << (1 << 1 | 0 << 0) | (1 << 1 | 0 << 0)))
        print(f"Current in {self.portal}")


traveler = TimeTravel(1 << (1 << (1 << 1 | 0 << 0) | (0 << 1 | 0 << 0)) | (0 << (1 << 1 | 1 << 0) | (1 << (1 << 1 | 0 << 0) | (0 << 1 | 0 << 0))))

for i in range(10):
    traveler.next_year()


"""
Find future_time

Current in Town C
Current in Metropolis E
Current in Village D
Current in Metropolis E
Current in Metropolis E
Current in Village D
Current in Village D
Current in Metropolis E
Current in Village D
Current in Town C
"""
print(traveler.future_time)

"""Fat Donut"""
import math
def fatdonut(r1,r2) :
    """Fat Donut"""
    area = (math.pi*r1*r1) - (math.pi*r2*r2)
    line = math.pi*r1*2 + math.pi*r2*2
    print(int(area))
    print(int(line))
fatdonut(int(input())/2,int(input())/2)

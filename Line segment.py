#LineSegmentTool

#Create your functions first

from math import sqrt

#Functions we need:
"""
# -line segment input
# -Line Segment Length
# -Line Segment Slope
# -Congruence
# -Parallel/perpendicular
"""

def lineIn(): #input
    #We want the final output to be: [[1,2],[3,4]]
    temp = []
    line = []
    for x in range(2):
        for y in range(2):
            temp.append(int(input(str(x)+','+str(y)+":")))
        line.append(list(temp))
        temp.clear()                
    return line

def length():
    #Formula for segment length:  sqrt(((x2-x1)**2) + ((y2-y1)**2))
    line = lineIn()
    return sqrt(((line[0][0]-line[1][0])**2) + ((line[0][1]-line[1][1])**2))

def slope():
    line = lineIn()
    #(y2-y1)/(x2-x1)
    return (line[0][1]-line[1][1])/(line[0][0]-line[1][0])

def congruent():
    #Equal Length?
    lengthA = length()
    lengthB = length()
    if lengthA == lengthB:
        print("The lines are congruent.")
    else:
        print("The lines are not congruent.")
    
def slopeCompare():
    #parallel or perpendicular or neither?
    slopeA = slope()
    slopeB = slope()

    if slopeA == slopeB:#Parallel case
        print("The lines are parallel")
    elif slopeA == -(1/slopeB):#Perp. (Compare slope A to neg. recip. of B)
        print("The lines are perpendicular")
    else:#No relationship
        print("The lines have no significant relationship")

print(slopeCompare())

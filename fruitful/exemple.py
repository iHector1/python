import math
def distance(x1,x2,y1,y2):
    dx=x2-x1
    dy=y2-x1
    dsquare=dx**2+dy**2
    result=math.sqrt(dsquare)
    return result

result=distance(12,78,3,89)
print(result)

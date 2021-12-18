import math
from swampy.TurtleWorld import *
def polygon(bob,length,degree): 
    rounds=int(360/degree)
    print(degree)
    print(int(degree))
    for i in range(rounds):
        fd(bob,length)
        rt(bob,degree)
def circule(t,r):
    circumference=2*math.pi*r
    n=50
    length=circumference/n
    polygon(t,n,length)
print('Inset radius')
radius=int(input())
world=TurtleWorld()
bob=Turtle()
bob.delay=0.01
circule(bob,radius)
wait_for_user()

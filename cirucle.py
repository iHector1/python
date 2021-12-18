from swampy.TurtleWorld import *
def circule(bob,lenght): 
    rounds=int(360/degree)
    print(degree)
    print(int(degree))
    for i in range(rounds):
        fd(bob,lenght)
        rt(bob,degree)
print('Inset lenght')
lenght=int(input())
world=TurtleWorld()
bob=Turtle()
bob.delay=0.01
circule(bob,lenght,degree)
wait_for_user()

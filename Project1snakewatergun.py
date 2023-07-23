#We are going to create a game of Snake Water Gun for the users
''' hey guys we are going to create our game application lets have a look at the code'''
import random
def gamewin(comp,you):
    if(comp==you):
        return None
    if(comp=='w'):
        if(you=='s'):
            return True
        elif(you=='g'):
            return False
    if (comp == 's'):
        if (you == 'g'):
            return True
        elif (you == 'w'):
            return False
    if (comp == 'g'):
        if (you == 'w'):
            return True
        elif (you == 's'):
            return False
randno=random.randint(1,3)
comp=print("Computer's turn:Snake(s),Water(w),Gun(g)")
if(randno==1):
    comp='s'
elif(randno==2):
    comp='w'
elif(randno==3):
    comp='g'
#print(f"Computer have chosen {comp}")  if we print computer choice then it will be a cheating this was just written to check whether our code is working properly or not
you=input("Your turn:Snake(s),Water(w),Gun(g)")
a=gamewin(comp,you)
if a==None:
    print("\nThis is a tie!")
elif a:
    print("\nCongrats You Win this game!")
else:
    print("\nAlas You lose!")
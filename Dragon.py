
import random,time
def displayintro():
    print(''' you are in a land full of dragons. In front of you,
     you see two caves.in one cave,the dragon is fiendly
     and will share his treasue with you. The other dragon
     is greedy and hungry,and will eat you on sight''')
    
    print()
def choosecave():
        cave=''
        while cave!=1 and cave!=2:
            print('Which cave will you go into?(1 or 2)')
            cave=input()
        return cave
def checkcave(chosencave):
    print('you approch the cave....')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He open his jaws and....')
    print()
    time.sleep(2)

    friendlycave=random.randint(1,2)

    if chosencave ==str(friendlycave):
        print('gives you his treasure')
    else:
        print('Gobbles you down in one bite!')
playagain='yes'
while playagain=='yes ' or playagain=='y':
    displayintro()
    cavenumber=choosecave()
    checkcave(cavenumber)      
    
    print('Do you want to play again?(yes or no)')
    playagain=input()      

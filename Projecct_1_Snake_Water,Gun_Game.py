import random


computer=random.choice([-1,0,1])
yourstr=input('Enter the choice(s/w/g):- ')
youdic={'snake':-1,'water':0,'gun':1}
computerdic={-1:'snake',0:'water',1:'gun'}
comp_choice=computerdic[computer]
you=youdic[yourstr]

print(f'Your choice is {yourstr} and \nComputer choice is {comp_choice}')
if computer==you:
    print("It's a drawing")
else:
    if (computer==-1 and you==0) or (computer==0 and you==1) or (computer==1 and you==-1):
        print("You lost. Try again next time")
    else:
        print("Congratulations, you won!")
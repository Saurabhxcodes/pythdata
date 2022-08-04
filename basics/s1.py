'''from random import randint
max_count =0
win_count = 0
loose_count = 0
dice = ['1','2','3','4','5','6']
while max_count<3:
    
    input("press enter 🤷‍♀️ to roll dice")
    out = randint(0,5)
    

    print(f' => {dice[out]}')
    
    if out == 6:
        win_count+=1
        max_count+=1
       
    if out ==6:
        win_count+=1
        max_count+=1
    
    if out==6:
        win_count+=1
        max_count+=1
    if max_count==3:
        break

          

        
    if win_count==3:
        print("you win 😊")
        break
    else:
        print("you loose")
        break 

    #STRINGS'''
import random
rolls = 50;
win_count =0
lose_count=0

for i in range(0, rolls):
    input("press enter 🤷‍♀️ to roll dice")
    die1 = random.randint(1,6)
    a=die1
    print(a)
    if die1==6:
       win_count+=1
    elif die1<=5:
        lose_count+=1
    if win_count==3:
        print("you win")
        break
    elif lose_count==3:
        print("you lost")
        break
#pip freeze 
#pip uninstall (cmnd name)
#pip install (commond name) 
#    













































































































































from random import randint
max_count =0
win_count = 0
loose_count = 0
dice = ['1','2','3','4','5','6']
while max_count<6:
    
    input("press enter 🤷‍♀️ to roll dice")
    out = randint(0,5,6)
    

    print(f' => {dice[out]}')
    if out == 6:
        win_count+=1
        max_count+=1
    elif out ==1:
        loose_count+=1
        max_count+1
    if win_count==3:
        print("you win 😊")
        break
    elif loose_count ==3:
        print("you loose")
        break 

    #STRINGS












































































































































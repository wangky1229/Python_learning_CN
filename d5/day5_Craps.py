import random

money = float(1000.00)

while True:
    print('You now have %f dollar' % money,end='\n')
    debt = float(input('Enter the debt of this ronund (try having more than 5000 dollar): '))
    if debt > money:
        print('You don not have enough money', end='\n')
        continue

    continue_dice = True
    s1 = 0
    round_nb = 0
    while continue_dice:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        s= dice1 + dice2
        if (s == 7 or s == 11) and s1 == 0:
            round_nb += 1
            money += debt
            print('Dice1: %d and Dice2: %d, sum = %d, player wins in round %d' % (dice1, dice2, s, round_nb), end='\n') 
            continue_dice = False
        elif (s == 2 or s == 3 or s == 12) and s1 == 0:
            round_nb += 1
            money -= debt
            print('Dice1: %d and Dice2: %d, sum = %d, player loses in round %d' % (dice1, dice2, s, round_nb), end='\n') 
            continue_dice = False
        elif s1 == s:
            round_nb += 1
            money += debt
            print('Dice1: %d and Dice2: %d, sum = %d (round 1 sum =%d), player wins in round %d' % (dice1, dice2, s, s1, round_nb), end='\n') 
            continue_dice = False
        elif s == 7 and round_nb >= 1:
            round_nb += 1
            money -= debt
            print('Dice1: %d and Dice2: %d, sum = %d (round 1 sum =%d), player loses in round %d because sum = %d' % (dice1, dice2, s, s1, round_nb, s), end='\n') 
            continue_dice = False
        elif s1 == 0:
            round_nb +=1
            s1 = s
            print('Round %d : sum = %d, no winner yet' % (round_nb,s), end='\n')
        else:
            round_nb +=1
            print('Round %d : sum = %d, no winner yet' % (round_nb,s), end='\n')
            
    if money == 0:
        print('Game over, you are broke', end='\n')    
        break
    elif money >= 5000:
        print('Mission complete, total money: %2f' % (money), end='\n')    
        break

        

 
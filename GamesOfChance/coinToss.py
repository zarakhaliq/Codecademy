import random
from random import randint

#Write your game of chance functions here
money=100

def coinToss(choice, bet) :
  
  #Zero=heads and 1=tails
  rand=random.randint(0,1)
  print("Heads or Tails?")
  if(bet>money):
    print("You don't have enough money.")
    print("---------------------")
    return 0
  if(bet<=0):
    print("Please bet higher.")
    print("---------------------")
    return 0
  if(choice=="heads"):
    print("Heads!")
  if(choice=="Tails"):
    print("Tails!")
  if ((choice=="heads") and (rand==0)):
    print(f'You won {bet} dollars')
    print("---------------------")
    return bet
  elif ((choice=="tails")and (rand==1)):
    print(f'You won {bet} dollars')
    print("---------------------")
    return bet
  else:
    print(f'You lost {bet} dollars')
    print("---------------------")
    return -bet



def rollTheDice(guess, bet) :
  
   dice1=random.randint(1, 6)
   dice2=random.randint(1, 6)
   sum=dice1+dice2
   #Checking if even
   even=sum%2==0
   #Checking if odd
   odd=sum%2!=0
   if(bet>money):
    print("You don't have enough money.")
    print("---------------------")
    return 0
   if(bet<=0):
    print("Please bet higher")
    print("---------------------")
    return 0
   print("Odd or Even? Choose one.")
   if(guess!="Odd" and guess!="Even") :
     print("Please choose Odd or Even.") 
     print("---------------------")
     return 0
   if(guess=="Even" and even):
        print(f'You chose {guess}.')
        print("Rolling the dice ...")
        print(f'The result is: {sum}')
        print(f'Congratulations! You won {bet} dollars.')
        print("---------------------")
        return bet
     
   elif(guess=="Odd" and odd):
        print(f'You chose {guess}.')
        print("Rolling the dice ...")
        print(f'The result is: {sum}')
        print(f'Congratulations! You won {bet} dollars.')
        print("---------------------")
        return bet

   else:
        print(f'You chose {guess}.')
        print("Rolling the dice ...")
        print(f'The result is: {sum}')
        print(f'You lost {bet} dollars. Better luck next time.')
        print("---------------------")
        return -bet

def cards(bet):
  #There are 13 cards per suit in a deck of cards:
  
  cards=[1,2,3,4,5,6,7,8,9,10,11,12,13]*4
  player1=random.choice(cards)
  player2=random.choice(cards)
  if(bet>money):
    print("You don't have enough money.")
    print("---------------------")
    return 0
  if(bet<=0):
    print("Please bet higher")
    print("---------------------")
    return 0
  print("Pick a card from the deck...")
  
  if(player1>player2):
    print(f'You picked {player1}')
    print("You won!")
    print(f'Player 1 wins {bet} dollars.')
    print("---------------------")
    return bet
  elif(player2>player1):
    print(f'You picked {player1}')
    print("You lose!")
    print(f'Player 1 lost {bet} dollars.')
    print("---------------------")
    return -bet
  else:
    print("It's a tie! Try again.")
    print("---------------------")
    return 0
    
def Roulette(oddOrEven, bet):
  #placing a bet on whether num odd or even
  #if odd and 0 or 00 generates:lose
  #if even and 0 or 00 generates: lose
 num=random.randint(0, 37)
 even=num%2==0
 odd=num%2!=0
 if(bet>money):
    print("You don't have enough money.")
    print("---------------------")
    return 0
 if(bet<=0):
    print("Please bet higher...")
    print("---------------------")
    return 0
 print("Hi, place a bet!")
 print("Odd or Even?")
 print(f'You chose {oddOrEven}')
 print("Spinning the wheel...")
 
 if(num==37):
   print("You landed on: 00")
 else:
   print(f'You landed on {num}')

 if(num==37 or num==0):
   print(f'Sorry, you lost {bet} dollars.')
   print("---------------------")
   return -bet
 if((oddOrEven=="Even") and (num==37 or num==0)):
    print(f'Sorry, you lost {bet} dollars.')
    print("---------------------")
    return -bet
 if((oddOrEven=="Odd") and (num==37 or num==0)):
    print(f'Sorry, you lost {bet} dollars.')
    print("---------------------")
    return -bet
 if(oddOrEven=="Even" and even):
    print(f'Congratulations! You just won {bet} dollars')
    print("---------------------")
    return bet
 elif(oddOrEven=="Odd" and odd):
    print(f'Congratulations! You just won {bet} dollars')
    print("---------------------")
    return bet
 else:
    print(f'Sorry, you lost {bet} dollars.')
    print("---------------------")
    return -bet

  








#Call your game of chance functions here

money+=coinToss("heads", 120)
money+=rollTheDice("Even", 10)
money+=cards(10)
money += Roulette("Even", 10)
print(f'Your total amount of money is {money}')
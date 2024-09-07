from dealer import *
import time
import random
import subprocess
import os

player_status = 'neutral'


home = True
bet = True
game = True
split = True
feedback = []
chip_total = 5000
betting = True




while home == True:
  game_key = int(input('This game is for players of the age of 18+, what is your age?\n'))
  if game_key < 18:
    print ('You are too young for this game, please try again when you are 18.')
    home == False
    
    continue
  else:
    print ('You are old enough for this game, enjoy!')
  
  ready = input ('Welcome to this free blackjack game! Would you like to play?".\n')
  if ready in ['No' , 'no', 'NO' , 'nO']:
    answer_1 = input ('We are sorry to hear that, Can you please tell us why? If you answered "No" by mistake, please type "x".\n')
    if answer_1 == 'x':
      continue
    else:
      print('Thankyou for your feedback, we will take it into consideration')
      (feedback.insert(0,answer_1))
      print (feedback)
      home == False
      continue
  elif ready in ['Yes' ,'yes' , 'YES']:
    print ('Enjoy!')
    print('I will deal you 2 cards, I will then ask you wether you would like to hit, stand, double down, or split. You can also take insurance if I have an ace and surrendor if you are not happy with your hand.')
    print('You will start with 5000 chips, use them wisely!\n')
  else: 
    print('Invalid answer, please try again.')
    continue

  while game == True:
    #This is where the game begins.
    J = 10
    Q = 10
    K = 10
    A = 11
    cards = [A,2,3,4,5,6,7,8,9,10,J,Q,K]
    #cards = [A,K]
    dealer_cards = [A,2,3,4,5,6,7,8,9,10,J,Q,K]



    see_chips = input('Would you like to see your chip total\n')
    if see_chips in ['yes' , 'Yes' , 'y' , ' YEs' , 'YES' , 'yES' , 'yeS']:
      print(f'Your chip total is {chip_total}')
    


    if chip_total <= 0:
      print ('\nYou have run out of chips, and have therefore lost \n.')
      break
    


    while betting == True:
      bet = int(input('How much would you like to bet?\n'))
      player_card_1 = random.choice(cards)
      player_card_2 = random.choice(cards)
      player_hand_total = player_card_1 + player_card_2
      if bet > chip_total:
        print("You don't have enough chips, please try again")
        betting = True
      else:
        print (f'You have bet {bet} chips') 
        betting = False
        chip_total = chip_total - bet
      
    
    player_hand = (f'{player_card_1},{player_card_2}')
    print (f'Your hand is {player_hand}')
    if player_hand_total == 21:
      payout = (bet*2.5)
      print (f'Blackjack! You have won {payout}')
      chip_total = chip_total + payout
      break






    elif player_card_1 == player_card_2:
      while split == True:
        decision_1 = input('Would you like to split? \n')
        if decision_1 in ['Yes' , 'YES' ,  'yes']:
          split_bet = int(input('You have chosen to split, how much would you like to bet on your second hand? You can only bet up to your original bet.\n'))
          if split_bet > bet:
            print ('You can only bet up to your previous bet, please try again.')
            continue
          chip_total = chip_total - split_bet
          if chip_total < 0:
            print ("You don't have enough chips to complete that action, please try again.")
            continue
          #this is where the split card sequence will be put in place
        elif decision_1 in ['No' , 'NO' , 'no']:
          print ('You have chosen to not split')
          split = False
          break
        else:
          print ('That is an invalid answer, please try again')
          continue






    else:   


      round_1 = True



      while round_1 == True:
        decision_1 = input('Would you like to hit, double down or stand?')
        if decision_1 in ['Hit' , 'HIT' , 'hit']:
          player_new_card = random.choice(cards)
          player_hand_total = int(player_hand_total) + int(player_new_card)


          if int(player_hand_total) > 21:
            print (f'Your hand total is {player_hand_total}, you have busted.\n')
            player_status = 'bust'
            round_1 == False
            break


          print (f'You have chosen to hit, your new card is:{player_new_card}')
          print (f'Your hand total is: {player_hand_total}\n')
          continue


        elif decision_1 in ['Stand', 'stand' , 'STAND']:
          
          player_new_card = 0
          print (f'Your total is {player_hand_total}\n')
          round_1 == False
          break


        else:
          print('Invalid answer, please try again')
          continue
      time.sleep(2)
      dealer_card_1 = random.choice(dealer_cards)
      dealer_card_2 = random.choice(dealer_cards)
      dealer_total = int(dealer_card_1) + int(dealer_card_2)
      dealer_hand = (f'{dealer_card_1},{dealer_card_2}')
      print (f"Dealer's hand is: {dealer_hand} \n Dealer's total is: {str(dealer_total)}")

      dealer_total = int(dealer_card_1) + int(dealer_card_2)



      if dealer_total == 21:
        dealer_status = 'blackjack'
        print ('\n Dealer has blackjack. You Lose')
    
      while dealer_total < 17:
        dealer_new_card = random.choice(dealer_cards)
        dealer_hand = (f'{dealer_card_1},{dealer_card_2},{dealer_new_card}')
        dealer_total = dealer_total + int(dealer_new_card)
        print (f"\nDealer Hits... \n \n Dealer's total is: {str(dealer_total)}\n" )
    

        next_dealer_round = str(input("Type 'y' to continue "))
        next_dealer_round_pass = True
    
        if dealer_total >= 17:
          break

        while next_dealer_round_pass == True:
          if next_dealer_round == 'y':
            break

          else:
            continue
      


      if dealer_total > 21:
        dealer_status = 'bust'
        print ('\n Dealer is bust!')

      if dealer_total >= 17:
        dealer_status = 'stand'
        print('\n Dealer stands.\n')
      

    if player_status == 'bust':
      print (f'You have lost this hand due to being bust.\n')
      chip_total = chip_total - bet
      betting = True
      round_1 == True
      split == True
      continue

    if dealer_status == 'bust':
      print ('You have won!')
      print (f'You have won {bet*2} chips!\n')
      chip_total = chip_total + bet*2
      betting = True
      round_1 == True
      split == True
      continue

    if dealer_total > player_hand_total:
      print (f'You have lost this hand due to having a lower total than the dealer.\n')
      chip_total = chip_total - bet
      betting = True
      round_1 == True
      split == True
      continue




    if dealer_total < player_hand_total:
      print ('You have won!')
      print (f'You have won {bet*2} chips!\n')
      chip_total = chip_total + bet*2
      betting = True
      round_1 == True
      split == True
      continue

    if dealer_total == player_hand_total:
      print ('You have pushed with the dealer\n')
      chip_total = chip_total + bet
      betting = True
      round_1 == True
      split == True
      continue
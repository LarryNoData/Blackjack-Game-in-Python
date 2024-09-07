import random
import time



J = 10
Q = 10
K = 10
A = 11
dealer_cards = [A,2,3,4,5,6,7,8,9,10,J,Q,K]
#dealer_cards = [A,K]
#dealer_cards = [2,3]
global dealer_status
dealer_status = 'neutral'

global dealer_total
dealer_total = 0

#dealers function

def Dealer():


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
    print('\n Dealer stands.')




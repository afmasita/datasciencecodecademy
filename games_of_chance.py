import random

money = 100

#Write your game of chance functions here
def coin_flip(guess, bet):
  if guess == "Heads":
    guess_code = 1
  elif guess == "Tails":
    guess_code = 2
  else:
    "Invalid bet! Enter Heads or Tails"    
  
  random_flip = random.randint(1,2)
  if random_flip == guess_code:
    return "You won " + str(2*bet)
  else:
    return "You lost " + str(bet)  

def cho_han(guess, bet):
  result = "None"
  if guess == "Even":
    expected_mod = 0
  elif guess == "Odd":
    expected_mod = 1
  else:
    return "Invalid bet! Enter Odd or Even"
  
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  sum_dice_mod_2 = (dice1 + dice2) % 2

  if sum_dice_mod_2 == expected_mod:
    print("You won " + str(2*bet))
  else:
    print("You lose " + str(bet)) 

def random_card(p1, p2, m1, m2):
  picked_card = []
  p1_card_num = random.randint(1,10)
  p1_card_sign = random.randint(1,4)
  #1-4: heart, diamond, club, spade
  picked_card.append((p1_card_num, p1_card_sign))

  p2_card_num = random.randint(1,10)
  p2_card_sign = random.randint(1,4)
  
  is_same = True
  while is_same:
    if p1_card_num == p2_card_num and p1_card_sign == p2_card_sign:
      p2_card_num = random.randint(1,10)
      p2_card_sign = random.randint(1,4)  
    else:
      picked_card.append((p2_card_num, p2_card_sign))
      is_same = False 
   
   # compare angka
  if p1_card_num == p2_card_num:
     print("It's a tie! " +  p1 + " and " + p2 +" got 0 dollars")
  else:
    if p1_card_num > p2_card_num:
      print(p1 + " won " + str(2*m1) + " dollars and " + p2 + " loses " + str(m2) + " dollars")
    else:
      print(p2 + " won " + str(2*m2) + " dollars and " + p1 + " loses " + str(m1) + " dollars") 

  print(p1 + "'s card: ", picked_card[0])
  print(p2 +  "'s card: ", picked_card[1])      

def roulette(guess, bet):
  # only for straight (single number) and odd/even guess

  roulette_list = list(range(0,37))
  roulette_list.append("00")
  ball = random.choice(roulette_list)
  is_even = False
  if ball % 2 == 0:
    is_even = True

  # reward
  match00 = str(3*bet)
  matchoddeven = str(bet)
  matchsinglenum = str(2*bet)
  match8 = str(3*bet)
  match30 = str(5*bet)

  print("Ball at " + str(ball) + "." )
  if guess == "Even":
    if is_even:
      print("You won " + matchoddeven)
    else:
      print("You lose "+ str(bet))
  elif guess == "Odd":
    if is_even:
      print("You lose "+ str(bet))
    else:
      print("You won " + matchoddeven)
  elif (guess >= 0 and guess <= 36) or guess == "00":         
    if guess == ball:
      if ball == "00":
        print("You won " + match00)
      elif ball == 8:
        print("You won " + match8)
      elif ball == 30:
        print("You won " + match30)
      else:
        print("You won " + matchsinglenum)
    else:
      print("You lose "+ str(bet))
  else:                 
    print("Your guess is invalid. Try again.")

#Call your game of chance functions here
print(coin_flip("Heads", money))
cho_han("Even", money)
random_card("Dara", "Nanda", 50, 80)
roulette(9, 100)
 


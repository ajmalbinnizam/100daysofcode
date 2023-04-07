import random
from art import logo
# from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pass_card(player, computer):
  display_result(player, computer)
  if sum(player) < sum(computer) and sum(computer) > 21:
    print("Opponent went over. You win 😁")
  elif sum(player) < sum(computer) and sum(player) < 21:
    print("You lose 😶")
  elif sum(computer) < sum(player) and sum(player) > 21:
    print("You win 🤞")
  
def display_result(player, computer):
  print(f"""\tYour final hand: {player}, final score: {sum(player)}
   \tComputer's final hand: {computer}, final score: {sum(computer)}""")

def black_jack(player, computer):
    if sum(computer) == 21:
      print("You lose, computer had a black jack")
      return True
    elif sum(player) == 21:
      print("You win, you got a black jack")
      return True
    else:
      return False


def start_game(player, computer):
  print(logo)
  first_time = True
  while(True):
    print(f"\tYour cards: {player}, current score: {sum(player)}")
    print(f"\tComputer's first card: {computer[0]}")
    if first_time:
      if black_jack(player, computer):
        break
      else:
        first_time = False
    
    if sum(player) == 21 and sum(computer) == 21:
      display_result(player, computer)
      print("Draw, better luck next time 👋")
      break
    elif sum(player) >= 21 and sum(computer) <= 21 or sum(player) >= 21 :
      display_result(player, computer)
      print("You went over. You lose 😭")
      break
    elif sum(computer) >= 21 and sum(player) <= 21 or sum(computer) >= 21:
      display_result(player, computer)
      print("You win 😊, computer went over")
      break 
    else:
      if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        another_card = True
        player.append(random.choice(cards))
        computer.append(random.choice(cards))
      else:
        computer.append(random.choice(cards))
        pass_card(player, computer)
        break
  play()

def play():
  if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    # clear()
    player = [random.choice(cards), random.choice(cards)]
    computer = [random.choice(cards), random.choice(cards)]
    start_game(player, computer)
  else:
    return

play()
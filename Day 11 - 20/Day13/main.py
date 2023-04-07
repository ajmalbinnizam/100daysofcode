from art import logo, vs
from game_data import data
import random
from replit import clear

def game_start(a, score):
  print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
  print(vs)
  b = random.choice(data)
  print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.')
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  if(a["follower_count"] > b["follower_count"] and answer == "a" or b["follower_count"] > a["follower_count"] and answer == "b"):
    score+=1
    clear()
    print(logo)
    print(f"You're right! Current score: {score}.")
    game_start(b, score)
  else:
    print(f"Sorry, that's wrong. Final score: {score}")

print(logo)
game_start(random.choice(data), 0)




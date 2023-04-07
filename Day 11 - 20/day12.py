''' Learning more about scopes and python have no block scope variable inside if while can be access from outside the ref'''
import random as random
def game_start(attempts):
  for i in range(attempts):
    print(f"You have {attempts - i} remaining")
    guess = int(input("Make a guess: "))
    if(guess - num > 0):
      print("Too high, Guess again")
    elif(guess - num < 0):
      print("Too low, Guess again")
    elif(num == guess):
      print(f"You got it! The answer was {num}")
      break
print("""Welcome to the Number Guessing Game!\n
I'm thinking of a number between 1 and 100.""")
num = random.randint(1, 100)    
print(f"Pssst, the correct answer is {num}")
level = input("Choose a difficulty. Type 'e' for easy or 'h' for hard: ")
if(level == 'e'):
  game_start(10)
else:
  game_start(5)
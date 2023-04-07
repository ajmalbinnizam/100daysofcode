import sys
import random
import hangman_art

hangman_art.print_logo()
stages = hangman_art.stages
lives = 6
live_index = 0

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
guessed_letters = []

for i in chosen_word:
  display.append("_")
print(display)
while "_" in display:
  guess = input("Guess a letter: ").lower()
  i = 0
  if guess in chosen_word:
    if guess in guessed_letters:
      print(f"uh oh, you already guessed '{guess}'")
      continue
    for letter in chosen_word:
      if letter == guess:
        display[i] = guess
        guessed_letters.append(guess)
      i+=1
    print(display)
  else:
    lives-=1
    live_index+=1
    if lives == 0:
      print("you lose, try again ")
      sys.exit(1)
    print(f"oops you lose a life \n {stages[live_index]} \nRemaining life {lives}\n")
  
print(f"You have won🥳\nThe Answer was {''.join(display)}")
sys.exit(1)



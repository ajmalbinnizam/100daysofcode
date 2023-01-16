import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
display = []
for i in chosen_word:
  display.append("_")

guess = input("Guess a letter: ").lower()

i = 0
for letter in chosen_word:
  if letter == guess:
    display[i] = guess
  else:
    print("Wrong")
  i+=1
print(display)


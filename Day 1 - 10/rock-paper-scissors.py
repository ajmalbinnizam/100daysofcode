import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
def print_shape(choice):
  if choice == "rock":
    print(rock)
  elif choice == "paper":
    print(paper)
  else:
    print(scissors)
    
user_point = 0
computer_point = 0
for i in range(3):
  print("what do you choose.. rock, paper, scissors\n")
  user = input("I choose: ")
  print_shape(user)
  item = ["rock", "paper","scissors"]
  computer = item[random.randint(0,2)]
  print(f"computer chose {computer}\n")
  print_shape(computer)
  if user == computer:
    print("DRAW no point for anyone\n")
  elif user == "rock" and computer == "scissors" or user == "paper" and computer == "rock" or user == "scissors" and computer == "paper":
    print("1 point for the user\n")
    user_point+=1
  elif computer == "rock" and user == "scissors" or computer == "paper" and user == "rock" or computer == "scissors" and user == "paper":
    print("1 point for the computer\n")
    computer_point+=1
  print(f"user: {user_point}\ncomputer: {computer_point}\n")
  
if user_point>computer_point:
  print(f"User wins: {user_point}")
    
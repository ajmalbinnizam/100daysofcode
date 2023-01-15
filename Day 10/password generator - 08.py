#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# for i in range(nr_letters): pwd.append(random.choice(letters))
# sample(list, item_number) returns a particular length list of items chosen from the sequence 
letter = random.sample(letters, nr_letters)
symbol = random.sample(symbols, nr_symbols)
number = random.sample(numbers, nr_numbers)

# concatenate the list
password = letter + symbol + number 
# shuffle the list to get a sequence of item
random.shuffle(password)
# string.join() joins iteratables in a list to string 
password = "".join(password)
print(f"Your password is: {password}")

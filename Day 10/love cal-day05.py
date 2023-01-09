print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

t = name1.lower().count("t") + name2.lower().count("t")
r = name1.lower().count("r") + name2.lower().count("r")
u = name1.lower().count("u") + name2.lower().count("u") 
e = name1.lower().count("e") + name2.lower().count("e")

true = t + r + u + e

l = name1.lower().count("l") + name2.lower().count("l") 
o = name1.lower().count("o") + name2.lower().count("o")
v = name1.lower().count("v") + name2.lower().count("v")
e = name1.lower().count("e") + name2.lower().count("e") 

love = l + o + v + e
score = int(str(t) + str(l))
if score <= 10 or score >=90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
    
    
# 🚨 max element in an array
student_scores = input("Input a list of student scores ").split()
highest = 0
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if(student_scores[n] >= highest):
      highest = student_scores[n]
print(student_scores)

print(f"The highest score in the class is: {highest}")



# 🚨 fizz buzz
for i in range(1, 101):
    if(i % 3 == 0) and (i % 5 ==0):
        print("FizzBuzz")
    elif(i % 3 == 0):
        print("Fizz")
    elif(i % 5 ==0):
        print("Buzz")
    else:
        print(i)
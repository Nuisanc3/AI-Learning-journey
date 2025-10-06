# input() = A function that prompts user to enter the data 
#           Returns the entered data as a string 

name = input("What is your name ? : ")
# age = input("How old are you ? ")
# age = int(age) 
# This is typecasting the input string to int, but there is smarter way!!! How?
# instead of "age = input("How old are you ? : ")" 
# we can use "age = int(input("How old are you ? : "))"

age = int(input("How old are you ? : "))

age = age + 1 

print(f"Hello {name} \nYou are {age} years old")



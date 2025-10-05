# This is my first program in Python
print("I like pizza")
print("It's really good")

###########################################################################################
####################################### NEW CONCEPT #######################################
###########################################################################################


# Variables = A Container for a value (string, integer, float, boolean)
#             A variable beahves as if it was the value it contains

# Strings
firstName = "Saumitra"
food = "burger"

# Integers 
age = 30
numberOfBurgersSaumitraCanEat = 3 

# float 
price = 249.50

# Boolean
isThisInfoTrue = True

# This is on the same lines as Java
print (firstName + " likes " + food + " alot")

# This is python specific 
print(f"{firstName} loves to eat {food}")
print(f"{firstName} is {age} years old and \ncan eat {numberOfBurgersSaumitraCanEat} {food}s in a day")
print(f"Each {food} is RS. {price} /-")
print(f"Is all the info checks out ? : {isThisInfoTrue}")

###########################################################################################
####################################### NEW CONCEPT #######################################
###########################################################################################

# Typecasting = The process of converting a variable from one data type to another
#               str(), int(), float(), bool

name = "Saumitra Kulkarni"
age = 30
gpa = 4.987654321
is_student = True
# profession = "AI/ML Developer"
profession = ""

gpa = int(gpa)



if is_student:
    age = str(age)
    age += "1"
    print(f"{name} is {age} years old and has gpa of {gpa}")
else :
    age = float(age)
    age += 1
    print(f"{name} is {age} years old; where 'age' is {type(age)}")


professionBoolean = bool(profession) 

if professionBoolean : 
    print (f"Professon is entered : {profession}")
else : 
    print ("Profession is not entered")


# Typecasting is useful for converting userinputs to different dataTypes
##########################################################################################






# Lesson ended at 21:00
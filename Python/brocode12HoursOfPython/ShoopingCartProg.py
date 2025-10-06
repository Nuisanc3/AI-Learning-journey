# Exercise 02 : Shooping cart program 

item = input("What are you tying to buy ? : ")
price  = float(input ("What's the price? : ") ) 
quantity = int(input("How many would you like ? : "))
total = price * quantity 

print(f"You have bought {quantity} x {item}/s\nYour total is : {total}")
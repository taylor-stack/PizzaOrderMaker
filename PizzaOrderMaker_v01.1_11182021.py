# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  elif size =="M":
    bill += 3
  else:
    bill += 3

if extra_cheese == "Y":
    bill += 1

final_bill = str(bill)

print("Your total bill is: $" + final_bill)

print("Thank you for choosing Python Pizza!")
print("Your order will be ready in 30 minutes. Do not forget to leave a tip for your delivery driver!")
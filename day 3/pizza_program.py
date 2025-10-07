print("Welcome to python pizza deliveries!")
bill = 0
size = input("What size of pizza do you want? S, M, or L: ")
if size == "S":
    bill += 15
    print("You will pay $ 5")
elif size == "M":
    bill += 20
    print("You will pay $ 7")
elif size == "L":
    bill += 25
    print("You will pay $ 10")
else:
    print("Wrong input")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 1

print(f"Your total pay is: ${bill}.")

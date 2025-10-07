# A and B, they both have to be true
# A or B, one of them has to be true for it to be true
# not A, reverses the conditions

print("Welcome to the rollercoaster!")
Height = int(input("What is your height in cm? "))
bill = 0
if Height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok, have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want your photo taken? Type y for yes and n for no.")
    if wants_photo == "y":
        #adding $3 to their bill for the photo
         bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride")


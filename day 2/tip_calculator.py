print("Welcome to the tip calculator!")
bill_total = float(input("What was the total bill $"))
tip_percentage = int(input("How much tip would you like to give? 10,12,or 15? "))
amount_to_tip = bill_total * (tip_percentage / 100)
people_paying = int(input("How many people to split the bill? "))
total_bill = bill_total + amount_to_tip
payment_for_one_person = total_bill / people_paying
final_amount = round(payment_for_one_person, 2)
#payment_per_person = input("Each person should pay:")
print(f"Each person should pay: ${final_amount}")

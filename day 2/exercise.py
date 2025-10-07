height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight/ height**2

print(bmi)

#round it to the nearest number
print(int(bmi)) #change it to integer
print(round(bmi)) #round function to the nearest whole number
print(round(bmi, 2)) #first is what you want to round, second is how many digits you want to round it to

#assignment function(to accumulate results of our operations)
score = 3
#so that you don't have to rewrite the variables
score -= 1 #operation then equals(-=,+=,*=, and /=)
print(score)

#f-strings (to concatenate different data types)
score = 3
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. Your winning is {is_winning}") #convert into a string and print it out, instead of doing it one by one

#checking the datatype
a = int("5") / int(2.7)
print(type(a))
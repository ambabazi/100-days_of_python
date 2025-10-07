#pulling each character individually from a string (subscripting)
print("Hello"[-1])

#string of numbers
print("1345")

#For mathematical operations, declare numbers as number datatype
#integer for whole numbers (either positive or negative)
print(134 +154) #addition

#large numbers (including commas) we use dashs in python
print(134_456_943)

#float for numbers with decimal points (floating point number)
print(3.141)

#boolean has 2 possible values "True and False"
print(True)
print(False)

#giving len data types that it accepts
len("448") #string

#knowing datatype of any variable(type checking)
print(type("helloo"))

#four lines to print type of what we have learnt
print(type(134)) #integer
print(type("hiii")) #string
print(type(3.14)) #float
print(type(True)) #boolean

#converting a datatype to a different one(type conversion or type casting)
print(int("4796") + int(1685))

#make the line run without errors
username =input("Enter your name")
length_of_username = len(username)
print("Number of letters in your name: " + str(length_of_username))

#other mathematical operators available
print(5 - 3) #substraaction
print(3 * 3) #multiplication
print(9 / 3) #division (use always get a float)
print(9 // 3) #prints out an integer (not recommended when you will need the decimal point)
print(3**3) #exponention

#order of priority for performing the mathematical operations is PEMDAS from left to right (Parentheses, expedition, multiplication, division, addition , and substraction)
#printing to get 3
print((3/3+3-3)*3)
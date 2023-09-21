#Simple 4 function (add, subtract, multiply, divide) calculator using Python. <-- These are called comments.

#Print statement which displays whatever you type on the screen, the words you want displayed must be in between "".
print("Select the operation being used: (+, -, *, /)")

#Here, 'operation' is a variable. -> A variable holds information. 
#input() takes the user input, meaning the user types something and we save it.
#Because we set the variable operation = input() the information stored in operation is whatever the user types.
operation = input()

print("Enter the first number:")
firstNum = float(input()) #A float are numbers that are decmials (ex. 3.14) We put float around the user input to convert 
                          #the user input into a float, or a decimal.

print("Enter the second number:")
secondNum = float(input()) #To make variables easier to read I use camelCase, where the first word is lowercase and the
                           #second is uppercase.

#PYTHON OPERATORS: 
# + -> add
# - -> subtract
# * -> multiply
# / -> divide

#If statements -> they make decisions for you.
if operation == "+":
    #if the user entered '+' as their operation, then add the two numbers they entered.
    print(firstNum + secondNum)
elif operation == "-":              #elif -> else if, if the first condition isn't satisfied, move to the next.
    print(firstNum - secondNum)
elif operation == "*":
    print(firstNum * secondNum)
elif operation == "/":
    print(firstNum/secondNum)
else:                               #else, if nothing is satisfied then print "INVALID OPERATOR"
    print("INVALID OPERATOR")

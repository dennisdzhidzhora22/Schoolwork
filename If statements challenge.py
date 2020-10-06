# First, pick any two numbers you like and store them in two separate variable, num1 & num2
num1 = float(input('Input a number: '))
num2 = float(input('Input another number: '))
# Next, create a valid condition that will check if num1 is greater than num2
if num1 > num2:
    print('The first number is greater than the second number. ')
# Next, create a second condition that will check if num1 is equal to the num2
if num1 == num2:
    print('The first number is equal to the second number. ')
# Finally, create a third condition that will check if num2 is greater than num1
if num2 > num1:
    print('The second number is greater than the first number. ')

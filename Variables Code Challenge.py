# ask a user to enter their first name and store it in a variable
firstname = input('Input your first name. ')
# ask a user to enter their last name and store it in a variable
lastname = input('Input your last name. ')
# print their full name
print(firstname + lastname)
# Make sure you have a space between first and last name
print(firstname + ' ' + lastname)
# Make sure the first letter of first name and last name is uppercase
print(firstname.upper() + ' ' + lastname.upper())
# Make sure the rest of the name is lowercase
print(firstname.capitalize() + ' ' + lastname.capitalize())

# Ask a user to enter a number
number1 = input('Enter a number. ')
# Ask a user to enter a second number
number2 = input('Enter another number. ')
# Calculate the total of the two numbers added together
add = (int(number1) + int(number2))
subt = (int(number1) - int(number2))
mult = (int(number1) * int(number2))
div = (int(number1) / int(number2))
# Print 'first number + second number = answer'
print(str(number1) + ' ' + '+' + ' ' + str(number2) + ' ' + '=' + ' ' + str(add))
# For example if someone enters 4 and 6 the output should read
# 4 + 6 = 10
# Continue these steps for subtraction, multiplication, and division
print(str(number1) + ' ' + '-' + ' ' + str(number2) + ' ' + '=' + ' ' + str(subt))
print(str(number1) + ' ' + '*' + ' ' + str(number2) + ' ' + '=' + ' ' + str(mult))
print(str(number1) + ' ' + '/' + ' ' + str(number2) + ' ' + '=' + ' ' + str(div))
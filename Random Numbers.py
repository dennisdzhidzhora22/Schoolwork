import random

# First random number
minimum = input('Input the minimum number for the first random number. ')
maximum = input('Input the maximum number for the first random number. ')
randomnumber1 = (random.randint(int(minimum), int(maximum)))
print('Your first random number is ' + str(randomnumber1) + '.')

# Second random number
minimum2 = input('Input the minimum number for the second random number. ')
maximum2 = input('Input the maximum number for the second random number. ')
randomnumber2 = (random.randint(int(minimum2), int(maximum2)))
print('Your second random number is ' + str(randomnumber2) + '.')

# Operation variables
add = (int(randomnumber1) + int(randomnumber2))
subt = (int(randomnumber1) - int(randomnumber2))
mult = (int(randomnumber1) * int(randomnumber2))
div = (int(randomnumber1) / int(randomnumber2))

# Operation prints
print('{} + {} = {}'.format(randomnumber1, randomnumber2, add))
print('{} - {} = {}'.format(randomnumber1, randomnumber2, subt))
print('{} * {} = {}'.format(randomnumber1, randomnumber2, mult))
print('{} / {} = {}'.format(randomnumber1, randomnumber2, div))




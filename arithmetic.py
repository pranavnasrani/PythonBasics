# todo arithmetic operators: +, -, *, /

a = 10
b = 3
print(round(a/b))

# ** indices
print(2**5)

# todo COMPARISON OPERATORS: ==, <, !=

# TO CHECK if number is even:
# We can use the modulo operator which sign is %. This will check the remainder.

num = input('Please enter a number ')

num = int(num)

if num % 2 == 0:
    print("The given number is even")
elif num % 3 == 0:
    print('The given number can be divided by 3 without a remainder.')
elif num % 5 == 0:
    print('The given number can be divided by 5 without a remainder.')
else:
    print("This number is not special at all")

# Sample Printing String
print("Hello world from Python")

# Booleans and printing
result = 3 < 10
print(type(result))
print(result)

# Strings
name = "Pranav Asrani"
print(name[0:2])

# Concatenation of inputted string
first_name1 = input("What is your first name? ")
last_name2 = input("What is your last name? ")
result = first_name1 + " " + last_name2
print(result)

# Concatenation Number with String
text = 'This is just text {} with value {}'
num1 = 21
num2 = 34
result = text.format(num1, num2)
print(result)

s = "0123456789"
print(s[1:8])  # This is normally printing letters 1-8 not including 8
print(s[1:8:3])  # This includes step size  of 3.

int_var = int(23.6)  # if float exist then python will round value down to make it an int
print(int_var)


# We have a int (integer type), float (decimal), str (text)
# We can also TODO transform int into str.

# for example:
c = str(198)  # this will convert the number into a string, which is useful for concatenation.


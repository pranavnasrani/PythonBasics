# TODO FOR LOOPS
name = "Kevin"

for letter in name:
    print(letter)
else:
    print("the letters were printed out")

# TODO WHILE LOOPS
index = 0
while index < len(name):
    print(name[index])
    index += 1
else:
    print('Finished with the while loop.')

# TODO NESTED LOOPS
print('\n now exploring nested loops.\nfor every outer_index increment, \nthere are three inner_index increments\n\n\n')
for outer_index in range(5):
    for inner_index in range(3):
        print('outer_index: ' + str(outer_index) + ' inner index: ' + str(inner_index))


# TODO ENUMERATE KEYWORD: USE indexes and values as well

index = 0
animals = ['cat', 'dog', 'rabbit', 'donkey', 'giraffe']
for index, value in enumerate(animals):
    print(str(index) + " " + str(value))


# What is concatenation

#first_name = 'James'
#middle_name = 'Bond'
#last_name = '777'
#age = 18
# James Bond 777

#print(first_name)
#print(middle_name)
#print(last_name)


#print(first_name + ' ' + middle_name + ' ' + last_name + ' ' + str(age))

# Casting is used to cast integer to string or vice versa
# str() function will cast age as a string so it can be added to the other strings


#Task: find out how to change 007 to int
#print(int(last_name))

# name = input('Please enter your name')
# print('Hello {}!'.format(name))


# get user data
# display message your age is +
# address - inc postcode and first line of address - house number


# # getting user data:
# # name
# name = input('Please enter your full name')
# print(f'Your name is {name}.')
# # DOB
# dob = input('Please enter your date of birth in the format DD/MM/YYYY')
# print(f'Your date of birth is {dob}')
# # age
# age = input('Please enter your age')
# print(f'You are {age} years old')

# # Address
# first_line = input('What is the first line of your address?')
# house_number = input('What is your house number?')
# post_code = input('What is your post-code?')

# print('Your address is ' + str(house_number) + ' ' + first_line + ', ' + post_code)

# # string slicing
# # indexing in python starts from 0
# greeting = "Hello World!"
# print(greeting[0:5])

# white_spaces = 'lots of spaces at the end                                                                  '
# print(len(white_spaces)) # returns length of white_spaces string = 91
# print(white_spaces.strip())
# print(len(white_spaces.strip())) # returns length of stripped string = 25

# count() method counts the numbers of times any word is available in the string
example_text = 'lots of text with some text'
print(example_text.count('text'))
print(example_text.replace('with', ',')) # replace the 'with' with ','
print(example_text.capitalize())
print(example_text.upper())
#Create 3 Variables to get user data

#name
name = input("What is your name? > ")

#DOB
dob = input("What is your DOB? > ")

#age
age = input("Please enter age: ")

print("Hi", name, "is am  correct to believe you are born on the following date? > " + dob,
      "and you are", age + ".")

print('name: {}, dob: {}, age: {}'.format(name, age, dob))

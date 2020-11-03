# Task Create a mixed data type list pf 7 items
# display the type of the data
# add, delete, replace, pop,
# use indexing to print the list in reverse order

memorable_information = ['emmanuel', 1960, 'fruits', 'African', 'rap', 1970, '199x']
print(type(memorable_information))

# add data
memorable_information.append("march")
print(memorable_information)

# delete
memorable_information.remove("fruits")
print(memorable_information)

# replace
memorable_information[3] = "Belgian"
print(memorable_information)

# pop
print(memorable_information.pop())

# reversing list
memorable_information.reverse()
print(memorable_information)

# Alternative way of reversing list
print(memorable_information[::-1])

print("\n")
# for loop printing is the type of each 'thing' in the list
for i in memorable_information:
    print(type(i))
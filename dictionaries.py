# What is a Dictionary ?

# Dictionary is a set of data which operate as a Key Value Pair
# Dictionaries (arrays) is another way of managing data but more dynamically.

# Syntax: {"key":"value", key:"value"}
# What type of data can we store/manage


# Dictionary #1
devops_student_data = {
    "name": "Emmanuel",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_name": ["operators", "data_types", "variables"]
}

print(type(devops_student_data))
print(devops_student_data)

# Name
print(devops_student_data["name"])

# changing name value
devops_student_data["name"] = "BabaJide"
devops_student_data["completed_lessons"] = 5
print(devops_student_data["name"])
print(devops_student_data["completed_lessons"])

print("\n")

# print keys or values from dict
print(devops_student_data.keys())
print(devops_student_data.values())
print(devops_student_data.items())
print("\n")

# How can we fetch the value called data types
print(devops_student_data["completed_lesson_name"][2])
print(devops_student_data["completed_lesson_name"][:1])
print(devops_student_data["completed_lesson_name"][:])

print("\n")

# Looping through the dictionary values
for key, value in devops_student_data.items():
    print(key + ':', value)


# TASK:
# create a new dict
# name, dob, address, course, grades
# create a list of hobbies of at least 3 items
# methods of dictionary remove, add, replace
# display data in reverse order of hobby list

new_dict = {
    "name":"Emmanuel",
    "dob":"12/12/12",
    "address":"Bromley rd",
    "course":"DevOps",
    "grades":"A",
    "hobbies":["table tennis", "manga", "football"]
}

# add
new_dict["new val"] = "hello world!"
# replace
new_dict["name"] = "john"
# reverse list
print(new_dict["hobbies"][::-1])
# remove
new_dict.pop("grades")

# dict_print
print(new_dict)

print("\n")

# loop print
for key, value in new_dict.items():
    print(key + ':', value)

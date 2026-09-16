# Day - Logical Operators

# 1. and
age = 20
has_id = True
print(age >= 18 and has_id) # True and True = True (can enter)

# 2. or
is_student = False
is_teacher = True
print(is_student or is_teacher) # False or True = True

# 3. not
is_rainy = False
print(not is_rainy) # not False = True

# Combine with relational operators (REAL USE)
marks = int(input("Enter your marks: "))
attendance = int(input("Enter attendance %: "))

# and example
print("\nEligible for exam?", marks >= 40 and attendance >= 75)

# or example
print("Need improvement?", marks < 40 or attendance < 75)

# not example
is_pass = marks >= 40
print("Failed?", not is_pass)

# Full logic like you will use in if-else
username = input("\nEnter username: ")
password = input("Enter password: ")

correct_user = "vinay"
correct_pass = "1234"

print("Login success?", username == correct_user and password == correct_pass)

# Extra - 3 conditions with and/or
a = 10
b = 20
c = 30
print("\nTricky:")
print(a < b and b < c) # True and True = True
print(a > b or b < c)  # False or True = True
print(not (a == 10))   # not True = False

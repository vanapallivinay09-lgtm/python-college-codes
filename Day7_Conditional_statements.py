# Day - Conditional Statements

# 1. Simple if
age = int(input("Enter age: "))
if age >= 18:
    print("You can vote")

# 2. if-else
marks = int(input("\nEnter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# 3. if-elif-else (most important)
print("\n--- Grade System ---")
marks = int(input("Enter marks (0-100): "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade F - Fail")

# 4. Using logical operators with if (connecting yesterday!)
print("\n--- Login Check (and) ---")
username = input("Username: ")
password = input("Password: ")

if username == "vinay" and password == "1234":
    print("Login Success")
else:
    print("Login Failed")

# 5. Nested if
print("\n--- Nested if ---")
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
    if num % 2 == 0:
        print("And it's Even")
    else:
        print("And it's Odd")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 6. Real-life example - like your CSS margin logic
print("\n--- Shopping Discount ---")
amount = int(input("Enter shopping amount: "))
if amount >= 5000:
    print("20% discount")
elif amount >= 2000:
    print("10% discount")
else:
    print("No discount")

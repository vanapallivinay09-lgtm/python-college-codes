# Day - Relational Operators

a = 10
b = 20

print("a =", a, "b =", b)
print("a == b:", a == b)  # False
print("a != b:", a != b)  # True
print("a > b:", a > b)    # False
print("a < b:", a < b)    # True
print("a >= 10:", a >= 10) # True
print("b <= 20:", b <= 20) # True

# With input (remember type conversion!)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nComparisons:")
print(num1, "==", num2, ":", num1 == num2)
print(num1, ">", num2, ":", num1 > num2)
print(num1, "<", num2, ":", num1 < num2)

# With strings - compares alphabetically
name1 = "Vinay"
name2 = "Vinay"
print("\nStrings:", name1 == name2) # True

# For if condition - you will use this next
age = int(input("\nEnter your age: "))
print("Are you 18 or above?", age >= 18)

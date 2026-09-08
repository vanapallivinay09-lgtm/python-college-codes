# Day - Type Conversions - Slicing, type(), Conversions

# 1. Slicing
word = "Python Programming"
print("Slicing:")
print(word[0:6]) # Python
print(word[7:])   # Programming
print(word[-11:]) # Programming
print(word[::-1]) # gnimmargorP nohtyP

# 2. type()
print("\ntype() checking:")
a = 10
b = 3.14
c = "Hello"
print(type(a), type(b), type(c))

user_input = input("\nEnter anything: ")
print("You entered:", user_input, "type is:", type(user_input))

# 3. Type Conversions
print("\nType Conversions:")
age = int(input("Enter your age: "))
print("After 5 years you will be:", age + 5)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum is:", num1 + num2)

# Extra - float and str
price_str = "49.99"
price = float(price_str)
print(price, type(price))
print("Price as int:", int(price))

marks = 95
print("My marks are " + str(marks)) # need str() to join with +

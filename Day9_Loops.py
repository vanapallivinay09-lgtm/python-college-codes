# Day - Loops

# 1. for loop - range
print("--- for loop ---")
for i in range(5): # 0 to 4
    print(i)

print("\n1 to 5:")
for i in range(1, 6): # 1 to 5
    print(i)

# 2. for with list (like HTML Lists ul/ol)
fruits = ["HTML", "CSS", "JavaScript"]
for fruit in fruits:
    print(fruit)

# 3. while loop
print("\n--- while loop ---")
count = 1
while count <= 5:
    print(count)
    count += 1 # very important, else infinite loop!

# 4. Real example - like you push to GitHub daily
print("\n--- Streak Counter ---")
days = int(input("How many days streak? "))
for day in range(1, days+1):
    print(f"Day {day}: Pushed code")

# 5. Loop + if (connecting yesterday's nested if!)
print("\n--- Even numbers 1-20 ---")
for num in range(1, 21):
    if num % 2 == 0: # nested if inside loop
        print(num, end=" ")

# 6. while with condition (like login retry)
print("\n\n--- Password Retry with while ---")
password = ""
while password != "1234":
    password = input("Enter password (1234 to exit): ")
    if password != "1234":
        print("Wrong, try again")

print("Login success!")

# 7. break and continue
print("\n--- break/continue ---")
for i in range(1, 6):
    if i == 3:
        continue # skip 3
    if i == 5:
        break # stop at 5
    print(i)

# 8. Table - most asked in college
n = int(input("\nEnter number for table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# Day - Nested Loops & Loop Control (break, continue, pass)

print("--- 1. Nested Loops ---")
# Outer loop = rows, Inner loop = columns
for i in range(1, 4): # 3 rows
    for j in range(1, 4): # 3 cols
        print(f"({i},{j})", end=" ")
    print() # new line after each row
# Output:
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)

print("\n--- Pattern with nested loops (like CSS card grid) ---")
# This is how you make pattern - interview favourite!
n = 5
for i in range(1, n+1):
    for j in range(i): # inner depends on outer
        print("*", end=" ")
    print()

# *
# * *
# * * *
# * * * *

print("\n--- Multiplication Table Grid (like HTML table) ---")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:2}", end=" ")
    print()

print("\n--- 2. break - Stop loop ---")
# Find first number divisible by 7
for num in range(1, 20):
    if num % 7 == 0:
        print(f"Found {num} divisible by 7 - break!")
        break # stop searching
    print(num, end=" ")

print("\n\n--- 3. continue - Skip ---")
# Print 1-10 but skip 5
for i in range(1, 11):
    if i == 5:
        print("(skip 5)", end=" ")
        continue # skip this iteration
    print(i, end=" ")

print("\n\n--- Skip even numbers (like filtering list) ---")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"{i} is odd")

print("\n--- 4. pass - Placeholder ---")
# You will use this when you know loop needed but not code yet
for i in range(5):
    if i == 2:
        pass # TODO: add logic later
    else:
        print(i, end=" ")

# Real example - login retry with break (like yesterday's nested if + loop)
print("\n\n--- Real: Login with 3 tries (break) ---")
correct_password = "1234"
for attempt in range(1, 4):
    pwd = input(f"Attempt {attempt}/3 - Enter password: ")
    if pwd == correct_password:
        print("Login Success!")
        break # exit loop, no more attempts
    else:
        print("Wrong password")
        if attempt == 3:
            print("Account locked - 3 tries over")
        else:
            continue # go to next attempt

print("\n--- Nested + break + continue together (like CSS Specificity battle) ---")
# Print numbers 1-20, but stop at 15, skip multiples of 3
for i in range(1, 21):
    if i > 15:
        print("\nReached 15 - break")
        break
    if i % 3 == 0:
        continue # skip 3,6,9,12,15
    print(i, end=" ")

print("\n\n--- Pattern with pass - for GitHub contribution grid ---")
for row in range(3):
    for col in range(7): # 7 days like GitHub graph
        if row == 1 and col == 3:
            print("[ ]", end=" ") # no commit
        else:
            print("[X]", end=" ") # commit done
    print()

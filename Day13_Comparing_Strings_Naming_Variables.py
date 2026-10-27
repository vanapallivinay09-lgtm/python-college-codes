# Day - Comparing Strings & Naming Variables

print("--- 1. Comparing Strings ---")

# == checks value, case-sensitive!
a = "Vinay"
b = "vinay"
print(a == b) # False - capital V vs small v
print(a.lower() == b.lower()) # True - after lower()

# !=
print("Python" != "Java") # True

# < > >= <= compares ASCII (dictionary order)
print("\n--- Dictionary Order (like HTML list sorting) ---")
print("apple" < "banana") # True - a comes before b
print("Apple" < "apple") # True - Capital A=65, small a=97 (ASCII)
print("abc" == "abc") # True
print("abc" < "abcd") # True - shorter is smaller if same start

# Real use - sorting names
names = ["Vinay", "Aman", "Zara", "Bobby"]
print("\nOriginal:", names)
print("Sorted:", sorted(names)) # alphabetically

# String comparison with if (like login)
print("\n--- Login check (case sensitive!) ---")
username = input("Enter username (Vinay): ")
if username == "Vinay": # must match exact case
    print("Exact match")
elif username.lower() == "vinay": # better - ignore case
    print("Match after lower() - case ignored")
else:
    print("No match")

# is vs == (interview question!)
print("\n--- is vs == ---")
s1 = "hello"
s2 = "hello"
print(s1 == s2) # True - values same
print(s1 is s2) # True - same memory (python optimizes small strings)

# But for list, different
list1 = ["a"]
list2 = ["a"]
print(list1 == list2) # True - values same
print(list1 is list2) # False - different memory locations
# Always use == for comparison, not is

print("\n--- 2. Naming Variables - Rules ---")

# ✅ GOOD NAMES
student_name = "Vinay" # snake_case - Python style
college_name = "NxtWave"
total_marks = 95
is_passed = True
MAX_ATTEMPTS = 3 # CONSTANT - capital

# ❌ BAD NAMES (will cause error or confusion)
# 1st_place = "Vinay" # can't start with number
# my-name = "Vinay" # hyphen not allowed, use underscore
# class = "10th" # 'class' is keyword - can't use
# print = "hi" # don't use built-in names!

# Python Keywords - can't use as variable
# if, else, for, while, def, class, import, True, False etc.

# Best practices - like CSS class naming!
print("\n--- Best Practices (like CSS .card) ---")
# CSS: .card, .btn-primary (kebab-case)
# Python: student_name, btn_primary (snake_case)

# Use meaningful names
# Bad:
x = 19
y = "Vinay"

# Good:
age = 19
name = "Vinay"

# For boolean, start with is_, has_, can_
is_logged_in = True
has_id_card = False
can_vote = age >= 18

print(f"Name: {name}, Age: {age}, Can vote: {can_vote}")

# Real example - combining comparison + good naming
print("\n--- Real Project Example ---")
github_username = input("Enter GitHub username: ").strip().lower()
correct_username = "vinay-lgtm"

if github_username == correct_username:
    print("Welcome to your hub!")
else:
    # Compare and suggest
    if github_username in correct_username:
        print(f"Did you mean {correct_username}?")
    else:
        print("Username not found")

# Length comparison
password = input("Enter password: ")
if len(password) < 8:
    print("Password too short - need 8+ chars")
elif len(password) == len("12345678"):
    print("Exactly 8 chars")
else:
    print("Good length")

print("\n--- Quick Test ---")
print("'Zebra' > 'Apple':", "Zebra" > "Apple") # True - Z after A
print("'10' > '2':", "10" > "2") # False! String compare, '1' < '2'
print("int('10') > int('2'):", int("10") > int("2")) # True - correct

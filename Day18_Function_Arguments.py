# Day - Function Arguments

print("--- 1. Positional Arguments (order matters!) ---")
def greet(name, age):
    print(f"Hello {name}, age {age}")

greet("Vinay", 19) # Vinay -> name, 19 -> age (position)
# greet(19, "Vinay") # WRONG - 19 goes to name!

print("\n--- 2. Keyword Arguments (name matters!) ---")
# Use name= value - order doesn't matter
greet(age=19, name="Vinay")
greet(name="Aman", age=20)

print("\n--- 3. Default Arguments ---")
def greet_default(name="Student", age=18):
    print(f"Hello {name}, age {age}")

greet_default("Vinay", 19)
greet_default("Aman") # age uses default 18
greet_default() # both default

# Rule: default must come AFTER normal
# def bad(a=5, b): -> Error!
# def good(a, b=5): -> OK

print("\n--- 4. *args - Many positional (tuple) ---")
# When you don't know how many arguments!
def add_all(*numbers):
    print(f"Got: {numbers}, type: {type(numbers)}")
    return sum(numbers)

print("Sum 1,2:", add_all(1, 2))
print("Sum 1,2,3,4,5:", add_all(1, 2, 3, 4, 5))
print("Sum no args:", add_all())

# Real - total marks
def total_marks(*marks):
    print(f"Marks: {marks}, Total: {sum(marks)}, Avg: {sum(marks)/len(marks)}")

total_marks(90, 85, 95)
total_marks(90, 85)

print("\n--- 5. **kwargs - Many keyword (dict) ---")
def show_profile(**info):
    print(f"Got: {info}, type: {type(info)}")
    for key, value in info.items():
        print(f"{key}: {value}")

show_profile(name="Vinay", age=19, branch="CSE")
show_profile(name="Aman", city="Hyderabad")

# Real - GitHub profile
def create_repo(**details):
    print("\nCreating repo with:")
    for k, v in details.items():
        print(f"  {k} = {v}")

create_repo(name="html-codes", visibility="public", language="HTML")

print("\n--- 6. All Together - Order! ---")
# Order: normal -> *args -> default -> **kwargs
# Actually: positional, default, *args, **kwargs

def full_example(name, age=18, *hobbies, **extra):
    print(f"\nName: {name}, Age: {age}")
    print(f"Hobbies: {hobbies}")
    print(f"Extra: {extra}")

full_example("Vinay", 19, "Coding", "Gaming", city="Hyderabad", college="【entity-NxtWave¦canonical_name=NxtWave】")

print("\n--- 7. Positional Only / Keyword Only (Python 3.8+) ---")
# / = before must be positional, * = after must be keyword
def example(a, b, /, c, *, d):
    print(f"a={a} (positional), b={b} (positional), c={c}, d={d} (keyword)")

example(1, 2, 3, d=4)
# example(a=1, b=2, c=3, d=4) # Error - a,b must be positional

print("\n--- 8. Real Project - Like Your Flexbox ---")
# Flexbox: flex: grow shrink basis - like function args!

def flex_box(grow=1, shrink=1, basis=0):
    return f"flex: {grow} {shrink} {basis}"

print("flex_box():", flex_box()) # defaults
print("flex_box(2):", flex_box(2)) # grow=2
print("flex_box(grow=2, basis=100):", flex_box(grow=2, basis=100))
print("flex_box(1, 0, 200):", flex_box(1, 0, 200))

# Your GitHub function
def push_file(file_name, repo="html-college-codes", *tags, **meta):
    print(f"\nPushing {file_name} to {repo}")
    print(f"Tags: {tags}")
    print(f"Meta: {meta}")

push_file("Day19_Flexbox.html")
push_file("Day18_Args.py", "python-college-codes", "python", "functions", day=18, streak="🔥")

print("\n--- 9. Interview Cheat Sheet ---")
print("Positional: greet('Vinay', 19) - order matters")
print("Keyword: greet(name='Vinay') - name matters")
print("Default: def greet(name='Student')")
print("*args: many positional -> tuple")
print("**kwargs: many keyword -> dict")

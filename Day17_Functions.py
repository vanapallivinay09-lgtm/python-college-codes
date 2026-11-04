# Day - Functions

print("--- 1. What is Function? ---")
# Function = reusable block like CSS .card class!
# Define once, use many times

# 2. Define function
def greet():
    print("Hello Vinay!")

# Call function
greet()
greet() # reuse!

print("\n--- 2. Function with Parameter ---")
def greet_person(name): # name = parameter
    print(f"Hello {name}!")

greet_person("Vinay")
greet_person("Aman")

# 2 parameters
def add(a, b):
    print(f"{a} + {b} = {a+b}")

add(5, 3)
add(10, 20)

print("\n--- 3. return vs print (Interview!) ---")

def add_print(a, b):
    print(a+b) # only prints

def add_return(a, b):
    return a+b # gives value back

result_print = add_print(5, 3) # 8 printed, but result = None
print("result_print:", result_print)

result_return = add_return(5, 3) # returns 8
print("result_return:", result_return)
print("Use return value:", result_return * 2) # can reuse!

print("\n--- 4. Real Examples - Like Your GitHub ---")

def create_github_repo(repo_name):
    repo_name = repo_name.strip().lower().replace(" ", "-")
    print(f"Created repo: {repo_name}")
    return repo_name

# Use it
my_repo = create_github_repo("  HTML College Codes ")
print(f"Saved as: {my_repo}")

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print("\nIs 4 even?", is_even(4))
print("Is 5 even?", is_even(5))

# Use in loop (like your streak)
for i in range(1, 6):
    if is_even(i):
        print(f"{i} even")

print("\n--- 5. Default Parameter ---")
def greet_with_default(name="Student"):
    print(f"Hello {name}")

greet_with_default("Vinay")
greet_with_default() # uses default

def power(base, exponent=2): # default square
    return base ** exponent

print("power(5):", power(5)) # 5^2=25
print("power(5,3):", power(5,3)) # 5^3=125

print("\n--- 6. Multiple Return Values ---")
def get_name_marks():
    return "Vinay", 95 # returns tuple

name, marks = get_name_marks()
print(f"Name: {name}, Marks: {marks}")

def calc(a, b):
    return a+b, a-b, a*b

sum_v, diff, prod = calc(10, 5)
print(f"Sum: {sum_v}, Diff: {diff}, Prod: {prod}")

print("\n--- 7. Functions + Lists (Super Combo) ---")

def get_topper(students):
    # students = [["Vinay",95], ["Aman",88]]
    topper = students[0]
    for s in students:
        if s[1] > topper[1]:
            topper = s
    return topper

students = [["Vinay", 95], ["Aman", 88], ["Zara", 92]]
top = get_topper(students)
print(f"Topper: {top[0]} - {top[1]} marks")

def clean_repos(repo_list):
    cleaned = [r.strip().lower() for r in repo_list]
    return cleaned

repos = ["  HTML-CODES ", " PYTHON CODES "]
print("Cleaned:", clean_repos(repos))

print("\n--- 8. Mini Project - GitHub File Counter ---")

def count_files(repo_name, days):
    return f"{repo_name} has {days} files"

def total_files(html_days, python_days):
    return html_days + python_days

html = 17
python = 16
print(count_files("html-college-codes", html))
print(count_files("python-college-codes", python))
print(f"Total Portfolio: {total_files(html, python)} files!")

# Function calling function (like nested if/loops)
def is_portfolio_ready(total):
    if total >= 20:
        return "Ready for Internship! 🔥"
    else:
        return "Keep building"

print(is_portfolio_ready(total_files(html, python)))

print("\n--- 9. Scope (Important!) ---")
x = 10 # global

def test():
    x = 5 # local - different!
    print("Inside function x:", x)

test()
print("Outside x:", x) # still 10

print("\n--- 10. Your Daily Use - Gen AI Debugging Function ---")

def debug_with_ai(code, error):
    print(f"Code: {code}")
    print(f"Error: {error}")
    print("AI Fix: Check syntax + add missing parts")

debug_with_ai("print('hi'", "SyntaxError: unexpected EOF")

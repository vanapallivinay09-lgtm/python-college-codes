# Day - Tuples

print("--- 1. What is Tuple? ---")
# List = [] - can change
# Tuple = () - CANNOT change!

my_list = ["HTML", "CSS", "JS"]
my_tuple = ("HTML", "CSS", "JS")

print("List:", my_list, type(my_list))
print("Tuple:", my_tuple, type(my_tuple))

my_list.append("Python") # works
print("List after append:", my_list)

# my_tuple.append("Python") # ERROR! 'tuple' has no append
# my_tuple[0] = "Java" # ERROR! Cannot change

print("\n--- 2. Creating Tuple ---")
t1 = (1, 2, 3)
t2 = 1, 2, 3 # without brackets also tuple!
t3 = ("Vinay",) # SINGLE item MUST have comma!
t4 = ("Vinay") # WITHOUT comma = string, not tuple!
t5 = () # empty tuple
t6 = tuple(["HTML", "CSS"]) # list -> tuple

print("t1:", t1, type(t1))
print("t2:", t2, type(t2))
print("t3 single:", t3, type(t3))
print("t4 no comma:", t4, type(t4)) # str!
print("t5 empty:", t5)
print("t6 from list:", t6)

print("\n--- 3. Access - Same as List ---")
skills = ("HTML", "CSS", "Python", "JS")
print("skills[0]:", skills[0])
print("skills[-1]:", skills[-1])
print("skills[1:3]:", skills[1:3]) # slicing - returns tuple
print("'Python' in skills:", "Python" in skills)
print("len:", len(skills))

for s in skills:
    print("Loop:", s)

print("\n--- 4. Tuple Methods - Only 2! ---")
# List has 11 methods, Tuple has ONLY 2!
nums = (1, 2, 2, 3, 2, 4)
print("nums:", nums)
print("count(2):", nums.count(2)) # 3 times
print("index(3):", nums.index(3)) # position 3
# That's it! No append, remove, sort...

print("\n--- 5. Unpacking - The Superpower! ---")
# Like you unpack a box
person = ("Vinay", 19, "CSE")
name, age, branch = person # unpack into 3 variables
print(f"Name: {name}, Age: {age}, Branch: {branch}")

# Swap without temp variable!
a = 10
b = 20
a, b = b, a # tuple magic!
print(f"After swap: a={a}, b={b}")

# Function returning many values
def get_profile():
    return "Vinay", 19, "Hyderabad" # returns tuple!

name2, age2, city = get_profile()
print(f"Profile: {name2}, {age2}, {city}")

print("\n--- 6. Tuple vs List - When to use? ---")
# Use TUPLE when data should NOT change
# Use LIST when data SHOULD change

# Example - Use Tuple:
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun") # never changes!
months = ("Jan", "Feb", "Mar") # never changes!
my_dob = (2006, 5, 15) # DOB never changes!
college_location = (17.45, 78.39) # lat, long - coordinates!

print("Days:", days)
print("DOB:", my_dob)
print("Location (lat, long):", college_location)

# Example - Use List:
my_skills = ["HTML", "CSS"] # will grow!
my_skills.append("Python")
print("My skills (list - grows):", my_skills)

print("\n--- 7. Nested Tuple + List Inside Tuple ---")
# Tuple inside Tuple
student = ("Vinay", (90, 85, 95), "CSE") # marks as tuple
print("Student:", student)
print("Marks:", student[1])
print("Mark 1:", student[1][0])

# List INSIDE tuple - list CAN change!
mixed = ("Vinay", [90, 85], "CSE")
mixed[1].append(100) # list inside CAN change!
print("List inside tuple changed:", mixed)

# Tuple INSIDE list
coords = [(10, 20), (30, 40), (50, 60)]
print("Coords list of tuples:", coords)
print("First coord x:", coords[0][0])

print("\n--- 8. Real Project - Your GitHub ---")
# Like your Flexbox: flex: 1 1 0 - fixed values = tuple!

def get_repo_info():
    return "html-college-codes", 19, "public" # tuple!

repo_name, days_count, visibility = get_repo_info()
print(f"Repo: {repo_name}, Days: {days_count}, Vis: {visibility}")

# Loop with enumerate - returns tuple!
for index, skill in enumerate(["HTML", "CSS", "Python"]):
    print(f"Day {index+1}: {skill}")

# Dictionary keys can be tuple, not list!
locations = {
    (17.45, 78.39): "Hyderabad",
    (28.61, 77.20): "Delhi"
}
print("Locations dict:", locations)
print("Hyderabad location:", locations[(17.45, 78.39)])

print("\n--- 9. Convert List <-> Tuple ---")
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print("List -> Tuple:", my_tuple)

back_to_list = list(my_tuple)
print("Tuple -> List:", back_to_list)

# Trick to 'change' tuple - convert, change, convert back
t = ("HTML", "CSS")
temp_list = list(t)
temp_list.append("Python")
t = tuple(temp_list)
print("Tuple 'changed' via list:", t)

print("\n--- 10. Interview Cheat Sheet ---")
print("List [] - Mutable (can change), 11 methods, slower")
print("Tuple () - Immutable (cannot change), 2 methods, FASTER")
print("Tuple unpacking: a, b = b, a (swap)")
print("Single tuple: ('Vinay',) - comma MUST")
print("Tuple = fixed data: days, DOB, coordinates, RGB")

# Day - Working With Lists (Advanced)

print("--- 1. List Methods Recap + New ---")
nums = [1, 2, 3]
nums.append(4) # end
print("append 4:", nums)

nums.insert(1, 99) # index, value
print("insert 99 at 1:", nums)

nums.extend([5, 6]) # add many at once (different from append!)
print("extend [5,6]:", nums)

# append vs extend - IMPORTANT!
a = [1,2]
a.append([3,4]) # [1,2,[3,4]] - adds as one item
print("\nappend [3,4]:", a)
b = [1,2]
b.extend([3,4]) # [1,2,3,4] - adds each item
print("extend [3,4]:", b)

print("\n--- 2. Removing - 3 ways ---")
langs = ["HTML", "CSS", "JS", "Python", "Java"]
print("Original:", langs)

langs.remove("JS") # by value
print("remove('JS'):", langs)

popped = langs.pop() # last
print(f"pop(): {popped}, list: {langs}")

popped2 = langs.pop(0) # index
print(f"pop(0): {popped2}, list: {langs}")

del langs[0] # by index - no return
print("del langs[0]:", langs)

langs.clear() # empty list
print("clear():", langs)

print("\n--- 3. Searching & Counting ---")
skills = ["HTML", "CSS", "Python", "CSS", "HTML"]
print(skills)
print("count('CSS'):", skills.count("CSS"))
print("index('Python'):", skills.index("Python")) # first occurrence
print("'Java' in skills:", "Java" in skills)
print("'HTML' in skills:", "HTML" in skills)

print("\n--- 4. Sorting - 2 ways ---")
numbers = [5, 1, 8, 2]
print("Original:", numbers)

numbers.sort() # changes original - no new list
print("sort() changes original:", numbers)

numbers = [5, 1, 8, 2]
new_sorted = sorted(numbers) # keeps original, returns new
print("sorted() keeps original:", numbers, "new:", new_sorted)

# Reverse sort
numbers.sort(reverse=True)
print("sort(reverse=True):", numbers)

print("\n--- 5. Copying - The Trap! ---")
# Wrong
list1 = [1, 2, 3]
list2 = list1 # same memory!
list2.append(4)
print("Wrong copy - list1 also changed:", list1) # [1,2,3,4] 😱

# Correct - 3 ways
list1 = [1, 2, 3]
list2 = list1.copy() # way 1
list3 = list1[:] # way 2 - slicing
list4 = list(list1) # way 3

list2.append(4)
print("Correct copy - list1 safe:", list1, "list2:", list2)

print("\n--- 6. Looping with Lists (like your HTML lists) ---")
html_days = ["Day1 Heading", "Day2 Colors", "Day3 Box Model", "Day14 Specificity", "Day15 Sizing"]

# Simple for
for day in html_days:
    print(day)

# With index - enumerate (best!)
print("\nWith enumerate:")
for i, day in enumerate(html_days, start=1):
    print(f"{i}. {day}")

# List comprehension - short way (interview favourite!)
print("\n--- 7. List Comprehension (Pro way) ---")
# Normal
squares = []
for n in range(1, 6):
    squares.append(n*n)
print("Normal:", squares)

# Comprehension - one line!
squares2 = [n*n for n in range(1, 6)]
print("Comprehension:", squares2)

# With if
even_squares = [n*n for n in range(1, 11) if n % 2 == 0]
print("Even squares 1-10:", even_squares)

# Real - clean GitHub repo names
repos = ["  html-college-codes ", " PYTHON-CODES ", "  css-day-15 "]
clean_repos = [r.strip().lower() for r in repos]
print("Cleaned repos:", clean_repos)

print("\n--- 8. Working with Lists - Real Project ---")
# Like your GitHub hub page

# Your repos
my_repos = ["html-college-codes", "python-college-codes"]

# Add new repo
new_repo = input("Enter new repo name: ").strip()
if new_repo not in my_repos:
    my_repos.append(new_repo)
    print(f"Added {new_repo}")
else:
    print(f"{new_repo} already exists!")

print(f"All repos: {my_repos}")

# Sort repos alphabetically
my_repos.sort()
print("Sorted repos:", my_repos)

# Count total files (like your streak)
total_files = 0
for repo in my_repos:
    if "html" in repo:
        total_files += 15 # you have 15 html files
    else:
        total_files += 14 # 14 python files

print(f"Total files across repos: {total_files}")

print("\n--- 9. Join & Split (List <-> String) ---")
# String -> List
sentence = "HTML CSS JavaScript"
lang_list = sentence.split() # split by space
print("split():", lang_list)

csv = "HTML,CSS,Python"
print("split(','):", csv.split(","))

# List -> String
joined = ", ".join(lang_list)
print("join:", joined)

print("\n--- 10. Nested Lists (2D List) ---")
# Like your Day 15 CSS min/max table
students = [
    ["Vinay", 95],
    ["Aman", 88],
    ["Zara", 92]
]

for student in students:
    name, marks = student # unpacking
    print(f"{name} - {marks} marks")
    if marks >= 90:
        print("  Grade A")

# Find topper
topper = students[0]
for s in students:
    if s[1] > topper[1]:
        topper = s
print(f"\nTopper: {topper[0]} with {topper[1]}")

print("\n--- Final - Your 15-day HTML + 14-day Python as Lists ---")
html_files = [f"Day{i}" for i in range(1, 16)]
python_files = [f"Day{i}" for i in range(1, 15)]
print(f"HTML: {len(html_files)} files, Python: {len(python_files)} files")
print(f"Total: {len(html_files + python_files)} files - Portfolio ready!")

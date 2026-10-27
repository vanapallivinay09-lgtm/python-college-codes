# Day - Lists (like HTML ul/ol but for Python)

print("--- 1. Creating Lists ---")
# List = [] can hold different types
fruits = ["apple", "banana", "mango"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Vinay", 19, 8.5, True] # like you store name, age, cgpa
empty = []

print(fruits)
print(f"First fruit: {fruits[0]}") # indexing like string! 0 = first

print("\n--- 2. Indexing & Slicing (same as Strings!) ---")
langs = ["HTML", "CSS", "JavaScript", "Python", "Java"]
print(langs[0]) # HTML
print(langs[-1]) # Java - last
print(langs[1:3]) # ['CSS', 'JavaScript'] - slicing
print(langs[:2]) # ['HTML', 'CSS']
print(langs[2:]) # from index 2 to end
print(langs[::-1]) # reverse!

print("\n--- 3. Changing Lists (Strings can't change, Lists can!) ---")
langs[0] = "HTML5" # change
print(langs)
langs.append("C++") # add at end - like push to 【entity-GitHub¦canonical_name=GitHub】!
print("After append:", langs)
langs.insert(1, "Bootstrap") # insert at position 1
print("After insert:", langs)

print("\n--- 4. Removing ---")
langs.remove("Java") # remove by value
print("After remove Java:", langs)
popped = langs.pop() # remove last
print(f"Popped: {popped}, Now: {langs}")
langs.pop(0) # remove index 0
print("After pop(0):", langs)
# del langs[0] # also works

print("\n--- 5. List Methods - Interview Favourites! ---")
nums = [5, 2, 8, 1, 9]
print("Original:", nums)
nums.sort() # sort ascending
print("sort():", nums)
nums.sort(reverse=True) # descending
print("sort(reverse=True):", nums)
nums.reverse() # reverse order
print("reverse():", nums)
print("len():", len(nums))
print("count(2):", [1,2,2,3].count(2))
print("'Python' in langs:", "Python" in langs)

print("\n--- 6. Looping Lists (for + list = super combo) ---")
# This is like your nested loops + CSS lists
html_skills = ["HTML", "CSS", "Box Model", "Flexbox"]
for skill in html_skills:
    print(f"- {skill}")

print("\nWith index:")
for i in range(len(html_skills)):
    print(f"Day {i+1}: {html_skills[i]}")

# Better way - enumerate
for index, skill in enumerate(html_skills, start=1):
    print(f"Day {index}: {skill}")

print("\n--- 7. List + Input (Real Project) ---")
# Like your GitHub repos list
my_repos = []
for i in range(3):
    repo = input(f"Enter repo {i+1} name: ")
    my_repos.append(repo.strip())

print("Your repos:", my_repos)

# Check if repo exists (like string comparison)
search = input("Search repo: ")
if search in my_repos:
    print(f"{search} found!")
else:
    print(f"{search} not found - create it!")

print("\n--- 8. Nested Lists (List inside List) ---")
# Like your HTML repo has many files
all_repos = [
    ["html-college-codes", "Day1", "Day2", "Day14"],
    ["python-college-codes", "Day1", "Day13"]
]
print(all_repos)
print("First repo name:", all_repos[0][0])
print("First repo Day2:", all_repos[0][2])

# Loop nested list
for repo in all_repos:
    print(f"\nRepo: {repo[0]}")
    for file in repo[1:]:
        print(f"  - {file}")

print("\n--- 9. String vs List ---")
# String split -> List, List join -> String (you learnt this!)
sentence = "HTML CSS Python"
langs_list = sentence.split() # " " split
print(langs_list) # ['HTML', 'CSS', 'Python']
new_sentence = " - ".join(langs_list)
print(new_sentence) # HTML - CSS - Python

print("\n--- 10. Copy Problem (Important!) ---")
# Don't do this
a = [1, 2, 3]
b = a # both point to same list!
b.append(4)
print("a:", a) # a also changed! [1,2,3,4]
print("b:", b)

# Do this - copy
a = [1, 2, 3]
b = a.copy() # or a[:]
b.append(4)
print("\nWith copy():")
print("a:", a) # [1,2,3] - safe
print("b:", b) # [1,2,3,4]

print("\n--- Final Task - Your Streak ---")
days = ["Day1 Arithmetic", "Day2 Variables", "Day3 Type Conv", "Day4 Relational", "Day5 Logical", "Day6 Conditional", "Day7 Nested If", "Day8 Loops", "Day11 Nested Loops", "Day12 Strings", "Day13 Lists"]
print(f"You have {len(days)} Python files!")
for d in days:
    if "Loop" in d:
        print(f"🔁 {d}")
    else:
        print(f"✅ {d}")

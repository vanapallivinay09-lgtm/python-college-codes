# Day - List Methods (Complete)

print("--- 1. Adding Methods ---")
langs = ["HTML", "CSS"]
print("Start:", langs)

langs.append("JS") # add 1 at end
print("append('JS'):", langs)

langs.extend(["Python", "Java"]) # add many at end
print("extend(['Python','Java']):", langs)

langs.insert(1, "Bootstrap") # insert at position
print("insert(1, 'Bootstrap'):", langs)

# append vs extend - INTERVIEW!
a = [1, 2]
a.append([3, 4])
print("\nappend([3,4]):", a) # [1,2,[3,4]] - nested!

b = [1, 2]
b.extend([3, 4])
print("extend([3,4]):", b) # [1,2,3,4] - flat!

print("\n--- 2. Removing Methods ---")
langs = ["HTML", "CSS", "JS", "Python", "Java", "CSS"]
print("Start:", langs)

langs.remove("CSS") # removes FIRST occurrence only
print("remove('CSS'):", langs) # only first CSS removed

popped = langs.pop() # last item
print(f"pop(): {popped}, list: {langs}")

popped2 = langs.pop(0) # index 0
print(f"pop(0): {popped2}, list: {langs}")

del langs[0] # delete by index - no return
print("del langs[0]:", langs)

# Clear
temp = langs.copy()
temp.clear()
print("clear():", temp)

print("\n--- 3. Searching Methods ---")
skills = ["HTML", "CSS", "Python", "CSS", "HTML"]
print("List:", skills)
print("index('Python'):", skills.index("Python")) # first index
print("index('CSS'):", skills.index("CSS")) # first CSS = 1
print("count('CSS'):", skills.count("CSS")) # 2 times
print("count('HTML'):", skills.count("HTML"))
print("'Java' in skills:", "Java" in skills)
print("len():", len(skills))

print("\n--- 4. Sorting Methods ---")
nums = [5, 2, 8, 1, 9]
print("Original:", nums)

nums.sort() # changes original!
print("sort():", nums)

nums.sort(reverse=True) # descending
print("sort(reverse=True):", nums)

# sorted() - keeps original (built-in function)
nums = [5, 2, 8]
new_sorted = sorted(nums)
print("\nsorted() - original safe:", nums, "new:", new_sorted)

# Reverse
nums.reverse() # reverse order in-place
print("reverse():", nums)

# Sort strings
langs = ["Python", "HTML", "CSS"]
langs.sort()
print("\nSort strings:", langs) # alphabetical: CSS, HTML, Python
langs.sort(key=len) # sort by length!
print("Sort by len:", langs) # CSS(3), HTML(4), Python(6)

print("\n--- 5. Copy Methods - The Trap! ---")
list1 = [1, 2, 3]
list2 = list1 # WRONG - same memory
list2.append(4)
print("Wrong copy - list1 also changed:", list1)

list1 = [1, 2, 3]
list2 = list1.copy() # CORRECT
list2.append(4)
print("Correct copy() - list1 safe:", list1, "list2:", list2)

list3 = list1[:] # slicing copy - also correct
list4 = list(list1) # list() copy
print("Slicing copy:", list3)

print("\n--- 6. All Methods Together - Real Project ---")
# Your 【entity-GitHub¦canonical_name=GitHub】 repos - like you manage files

my_repos = ["html-college-codes"]
print("Start:", my_repos)

# Add
my_repos.append("python-college-codes")
my_repos.extend(["css-practice", "js-practice"])
print("After append+extend:", my_repos)

# Insert at top
my_repos.insert(0, "my-first-website")
print("After insert(0):", my_repos)

# Remove one
my_repos.remove("js-practice")
print("After remove('js-practice'):", my_repos)

# Sort
my_repos.sort()
print("After sort():", my_repos)

# Count and index
print(f"Total repos: {len(my_repos)}")
print(f"Index of python repo: {my_repos.index('python-college-codes')}")

# Pop last for demo
last = my_repos.pop()
print(f"Popped last: {last}, remaining: {my_repos}")

# Copy for backup
backup = my_repos.copy()
backup.append("backup-repo")
print(f"Original: {my_repos}, Backup: {backup}")

print("\n--- 7. List Methods Cheat Sheet ---")
print("append(x)  - add 1 at end")
print("extend([..]) - add many at end")
print("insert(i,x) - add at position")
print("remove(x)  - remove by value (first)")
print("pop(i)     - remove by index (returns)")
print("del list[i] - remove by index")
print("clear()    - empty list")
print("index(x)   - find position")
print("count(x)   - how many times")
print("sort()     - sort in-place")
print("reverse()  - reverse in-place")
print("copy()     - copy list")

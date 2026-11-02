# Day - Working with Lists & Strings Together

print("--- 1. String -> List (split) ---")
sentence = "I love HTML CSS Python"
words = sentence.split() # split by space
print(words) # ['I', 'love', 'HTML', 'CSS', 'Python']

csv = "html-college-codes,python-college-codes,css-day-16"
repos = csv.split(",")
print(repos)

# Split with maxsplit
date = "2025-11-02"
print(date.split("-", 1)) # ['2025', '11-02']

print("\n--- 2. List -> String (join) ---")
langs = ["HTML", "CSS", "JavaScript"]
print(" ".join(langs)) # HTML CSS JavaScript
print(", ".join(langs)) # HTML, CSS, JavaScript
print(" - ".join(langs)) # HTML - CSS - JavaScript
print("".join(langs)) # HTMLCSSJavaScript

# Real - GitHub README generation
files = ["Day1", "Day2", "Day3"]
readme_line = " | ".join(files)
print(f"README: {readme_line}")

print("\n--- 3. List of Strings - String methods on each ---")
names = ["  vinay ", " AMAN ", " Zara "]
print("Original:", names)

# Clean each - using loop (like you clean GitHub usernames)
cleaned = []
for name in names:
    cleaned.append(name.strip().lower().title())
print("Cleaned:", cleaned)

# Same with list comprehension - pro way!
cleaned2 = [n.strip().lower().title() for n in names]
print("Comprehension:", cleaned2)

print("\n--- 4. String methods that return List ---")
text = "html css python"
print("split():", text.split())
print("split('s'):", text.split("s"))

email = "vinay@gmail.com"
username, domain = email.split("@")
print(f"Username: {username}, Domain: {domain}")

# Partition
print("\npartition():", "html-css-python".partition("-")) # ('html', '-', 'css-python')

print("\n--- 5. Searching - in (both) ---")
# String
print("'CSS' in 'HTML CSS':", "CSS" in "HTML CSS")
# List
print("'CSS' in ['HTML','CSS']:", "CSS" in ["HTML", "CSS"])

# Count
print("\nCount:")
print("'l' in 'hello':", "hello".count("l"))
print("'CSS' in ['HTML','CSS','CSS']:", ["HTML","CSS","CSS"].count("CSS"))

print("\n--- 6. Looping - String is also list of chars! ---")
word = "Python"
for char in word:
    print(char, end=" ")

print("\n\nList loop:")
for lang in ["HTML", "CSS"]:
    for char in lang:
        print(f"{lang}: {char}")

print("\n--- 7. Working Together - Real Project ---")
# Like your html-college-codes files list

# You have this string from GitHub
file_string = "Day1_Heading,Day2_Colors,Day3_BoxModel,Day14_Specificity,Day15_Sizing,Day16_BoxSizing"
print("Raw:", file_string)

# Convert to list
file_list = file_string.split(",")
print("List:", file_list)

# Clean and filter only Day15+
filtered = []
for f in file_list:
    if "Day15" in f or "Day16" in f:
        filtered.append(f.strip())

print("Filtered Day15+:", filtered)

# Sort
filtered.sort()
print("Sorted:", filtered)

# Join back to string for README
final_string = " -> ".join(filtered)
print("Final for README:", final_string)

print("\n--- 8. Reversing - Both! ---")
s = "Vinay"
print("String reverse [::-1]:", s[::-1])
lst = ["HTML", "CSS", "JS"]
print("List reverse [::-1]:", lst[::-1])
lst.reverse() # in-place
print("List reverse():", lst)

print("\n--- 9. Comparing - String vs List (Important!) ---")
# String immutable, List mutable
my_string = "Vinay"
# my_string[0] = "v" # ERROR - can't change string!

my_list = ["V", "i", "n", "a", "y"]
my_list[0] = "v" # Works!
print("List after change:", my_list)
print("String from list:", "".join(my_list)) # v + inay = vinay

# How to "change" string - create new
my_string = "Vinay"
my_string = "v" + my_string[1:]
print("New string:", my_string)

print("\n--- 10. Mini Project - GitHub Stats ---")
# Combined skills from Day 12, 13, 14, 15

repos_data = "html-college-codes:16,python-college-codes:15"
print("Data:", repos_data)

# Parse
repos = repos_data.split(",")
total = 0
for repo in repos:
    name, count = repo.split(":")
    count = int(count)
    total += count
    print(f"{name.strip()} -> {count} files - {'🔥 Streak!' if count > 10 else ''}")

print(f"Total files: {total} - Portfolio ready!")

# Create list of all days
all_days = [f"Day {i}" for i in range(1, total+1)]
print(f"\nAll days list length: {len(all_days)}")
print("First 3:", all_days[:3])
print("Last 3:", all_days[-3:])

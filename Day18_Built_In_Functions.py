# Day - Built-in Functions (Python gives you free!)

print("--- 1. You Already Know These ---")
# print(), input(), len(), type(), int(), str(), float()
name = "Vinay"
print("print():", name)
print("len():", len(name))
print("type():", type(name))
print("str():", str(95))
print("int():", int("95"))

print("\n--- 2. Math Built-ins ---")
nums = [5, 2, 8, 1, 9]
print("max():", max(nums)) # 9 - biggest
print("min():", min(nums)) # 1 - smallest
print("sum():", sum(nums)) # 25 - total
print("sorted():", sorted(nums)) # [1,2,5,8,9] - sorted new
print("reversed():", list(reversed(nums)))

print("abs(-10):", abs(-10)) # 10 - distance from 0
print("round(3.567, 2):", round(3.567, 2)) # 3.57
print("pow(2, 3):", pow(2, 3)) # 8 - 2^3

print("\n--- 3. Type Conversion Built-ins (Day 3!) ---")
print("int('123'):", int("123"))
print("float('99.5'):", float("99.5"))
print("str(123):", str(123))
print("bool(0):", bool(0)) # False
print("bool(1):", bool(1)) # True
print("bool(''):", bool("")) # False - empty
print("bool('Vinay'):", bool("Vinay")) # True
print("list('Vinay'):", list("Vinay")) # ['V','i','n','a','y']
print("tuple([1,2]):", tuple([1,2]))

print("\n--- 4. String + List Built-ins ---")
text = "html css python"
print("text.upper():", text.upper())
print("text.split():", text.split())

langs = ["HTML", "CSS"]
print("enumerate():")
for i, lang in enumerate(langs, start=1):
    print(f"{i}. {lang}")

print("\nzip() - combine 2 lists:")
names = ["Vinay", "Aman"]
marks = [95, 88]
for n, m in zip(names, marks):
    print(f"{n}: {m}")

print("\n--- 5. Input/Output Built-ins ---")
# input() always returns string - you know!
# print() with sep and end
print("A", "B", "C", sep=" - ") # A - B - C
print("Hello", end=" ")
print("World on same line!") # end=" " instead of \n

# print with f-string
age = 19
print(f"My name is {name}, age {age}")

print("\n--- 6. Helpful Built-ins - Interview Favourites ---")
print("range(5):", list(range(5)))
print("range(1, 10, 2):", list(range(1, 10, 2))) # odd numbers

# id() - memory address
print("\nid(name):", id(name))

# isinstance - check type
print("isinstance(95, int):", isinstance(95, int))
print("isinstance('Vinay', str):", isinstance("Vinay", str))

# all / any - like and/or for list
scores = [True, True, False]
print("\nall():", all(scores)) # False - all must be True
print("any():", any(scores)) # True - one True is enough

# Same as logical operators you learnt!
# all = and, any = or

print("\n--- 7. Real Project - Using Built-ins ---")

# Your 【entity-GitHub¦canonical_name=GitHub】 repos
repos = ["html-college-codes", "python-college-codes"]
files = [17, 16]

print(f"Total repos: {len(repos)}")
print(f"Max files: {max(files)} in {repos[files.index(max(files))]}")
print(f"Min files: {min(files)}")
print(f"Total files: {sum(files)}")

# Clean and sort
messy = ["  HTML ", " python ", " CSS "]
clean = sorted([m.strip().lower() for m in messy])
print("Cleaned + Sorted:", clean)

# Check if all files > 10
print("All repos > 10 files?", all(f > 10 for f in files))
print("Any repo > 15 files?", any(f > 15 for f in files))

# Upper case all repo names
upper_repos = list(map(str.upper, repos))
print("Upper repos (map):", upper_repos)

print("\n--- 8. Built-in vs Custom Function ---")
# Built-in: print(), len(), max() - already defined by Python
# Custom: def greet(): - you define

def my_max(a, b): # custom - you wrote
    if a > b:
        return a
    return b

print("Custom my_max(5,10):", my_max(5, 10))
print("Built-in max(5,10):", max(5, 10)) # same but Python did it

print("\n--- 9. Most Used Built-ins - Cheat Sheet ---")
print("len(), print(), input(), type(), int(), str(), float()")
print("max(), min(), sum(), sorted(), reversed()")
print("range(), enumerate(), zip(), abs(), round(), list(), tuple()")

print("\n--- 10. Practice - Your 33 files ---")
html_days = list(range(1, 18)) # 1-17
python_days = list(range(1, 17)) # 1-16
print(f"HTML days: {len(html_days)}, Python days: {len(python_days)}")
print(f"Total: {sum([len(html_days), len(python_days)])}")
print(f"Top: Day {max(html_days + python_days)}")

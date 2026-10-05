# Day - String Methods

name = "  Vinay Kumar  "
print("Original:", f"'{name}'")

# 1. Case methods
print("\n--- Case ---")
print("lower():", name.lower())
print("upper():", name.upper())
print("title():", name.title()) # First letter capital
print("capitalize():", "vinay kumar".capitalize())

# 2. Strip - remove spaces
print("\n--- Strip (like margin) ---")
print("strip():", f"'{name.strip()}'") # both sides
print("lstrip():", f"'{name.lstrip()}'") # left
print("rstrip():", f"'{name.rstrip()}'")

# 3. Search methods
text = "I love HTML and Python"
print("\n--- Search ---")
print("find('Python'):", text.find("Python")) # index
print("find('Java'):", text.find("Java")) # -1 if not found
print("'HTML' in text:", "HTML" in text) # True/False
print("startswith('I love'):", text.startswith("I love"))
print("endswith('Python'):", text.endswith("Python"))

# 4. Replace & Count
print("\n--- Replace & Count ---")
print("replace:", text.replace("Python", "CSS"))
print("count('o'):", text.count("o"))

# 5. Split & Join - MOST IMPORTANT
print("\n--- Split & Join (like HTML Lists) ---")
langs = "HTML,CSS,JavaScript,Python"
print("split(','):", langs.split(",")) # string -> list
words = ["HTML", "CSS", "JS"]
print("join:", "-".join(words)) # list -> string

# 6. is methods - for validation
print("\n--- Validation ---")
print("'123'.isdigit():", "123".isdigit())
print("'abc'.isalpha():", "abc".isalpha())
print("'abc123'.isalnum():", "abc123".isalnum())

# 7. Real example - like you clean GitHub username
print("\n--- Real Use ---")
username = input("Enter username with spaces: ") # "  Vinay  "
clean = username.strip().lower() # "vinay"
print(f"Cleaned username for GitHub: '{clean}'")

# Check password
password = input("Enter password: ")
if len(password) >= 8 and not password.isalpha():
    print("Strong password")
else:
    print("Weak password")

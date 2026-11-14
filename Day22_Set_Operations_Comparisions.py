# Day - Set Operations & Set Comparisons

print("--- 1. What is Set? Quick Revision ---")
# Set = {} - no duplicates, no order, no index
s = {1, 2, 2, 3, 3, 3}
print("Set removes duplicates:", s) # {1,2,3}

my_skills = {"HTML", "CSS", "Python"}
friend_skills = {"CSS", "JS", "Python", "Java"}
print("My:", my_skills)
print("Friend:", friend_skills)

print("\n--- 2. UNION - | or union() - ALL (no duplicate) ---")
# Like you combine 2 GitHub repos
print("Union | :", my_skills | friend_skills)
print("Union method:", my_skills.union(friend_skills))
# HTML, CSS, Python, JS, Java - all!

print("\n--- 3. INTERSECTION - & or intersection() - COMMON ---")
# What both know?
print("Intersection & :", my_skills & friend_skills)
print("Intersection method:", my_skills.intersection(friend_skills))
# CSS, Python - common!

print("\n--- 4. DIFFERENCE - - or difference() ---")
# What I know but friend DOESN'T
print("Me - Friend:", my_skills - friend_skills) # HTML only
print("Friend - Me:", friend_skills - my_skills) # JS, Java
# Order matters! A-B != B-A

print("\n--- 5. SYMMETRIC DIFFERENCE - ^ - Only One Side ---")
# In one but NOT both
print("Symmetric ^ :", my_skills ^ friend_skills)
print("Method:", my_skills.symmetric_difference(friend_skills))
# HTML, JS, Java - CSS, Python removed (both have)

print("\n--- 6. Set Comparisons - issubset, issuperset, disjoint ---")

a = {1, 2}
b = {1, 2, 3, 4}
c = {5, 6}

print("a:", a, "b:", b, "c:", c)
print("a issubset of b:", a.issubset(b)) # True - a inside b?
print("a <= b:", a <= b) # same - subset
print("b issuperset of a:", b.issuperset(a)) # True - b contains a?
print("b >= a:", b >= a) # same
print("a isdisjoint c:", a.isdisjoint(c)) # True - NO common?
print("a isdisjoint b:", a.isdisjoint(b)) # False - have common

# Proper subset vs subset
print("a < b (proper):", a < b) # True - a smaller and inside b
print("b < b (proper):", b < b) # False - equal not proper
print("b <= b:", b <= b) # True - equal is subset

print("\n--- 7. Real Project - Your College Skills ---")
all_students = {"Vinay", "Aman", "Priya", "Rahul", "Sneha"}
python_class = {"Vinay", "Aman", "Priya"}
html_class = {"Vinay", "Priya", "Rahul"}

print("All:", all_students)
print("Python class:", python_class)
print("HTML class:", html_class)

print("\nBoth classes (Intersection):", python_class & html_class)
print("Any class (Union):", python_class | html_class)
print("Only Python not HTML:", python_class - html_class)
print("Only HTML not Python:", html_class - python_class)
print("Only one class:", python_class ^ html_class)

# Check
print("\nIs python_class subset of all?", python_class.issubset(all_students))
print("Is python & html disjoint?", python_class.isdisjoint({"Sneha"}))

print("\n--- 8. Updating Sets - |=, &=, -=, ^= ---")
skills = {"HTML", "CSS"}
skills |= {"Python", "JS"} # union update
print("After |= Python,JS:", skills)

skills &= {"HTML", "Python", "Java"} # intersection update - keep only common
print("After &= HTML,Python,Java:", skills)

skills -= {"HTML"} # difference update
print("After -= HTML:", skills)

skills ^= {"Java", "Python"} # symmetric update
print("After ^= Java,Python:", skills)

print("\n--- 9. Venn Diagram in Code ---")
# Like school Maths Venn diagram

# College fest
cricket = {"Vinay", "Aman", "Rahul"}
football = {"Aman", "Priya", "Sneha"}
print("Cricket:", cricket)
print("Football:", football)
print("Both games:", cricket & football) # Aman
print("At least one:", cricket | football)
print("Only cricket:", cricket - football)
print("Only football:", football - cricket)
print("Only one game:", cricket ^ football)
print("Neither? Total 5 students, playing:", len(cricket | football))

print("\n--- 10. Interview Cheat Sheet ---")
print("Union | : All")
print("Intersection & : Common")
print("Difference - : Only in first")
print("Symmetric ^ : Only in one, not both")
print("issubset / <= : Is inside?")
print("issuperset / >= : Does it contain?")
print("isdisjoint : No common at all?")
print("Proper subset < : Inside + smaller")

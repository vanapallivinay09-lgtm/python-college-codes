# 1. String Concatenation (+)
first = "Vinay"
last = "LGTM"
full = first + " " + last
print(full) # Vinay LGTM

# 2. String Repetition (*)
print("Hi! " * 3) # Hi! Hi! Hi!

# 3. Input and Output functions
name = input("Enter your name: ")
print("Hello", name) # output with comma adds space

# 4. String Index - index starts from 0
word = "Python"
print(word[0]) # P
print(word[1]) # y
print(word[-1]) # n (last letter)
print(word[0:4]) # Pyth (0 to 3)

# Task for you - try this:
s = input("Enter a word: ")
print("First letter:", s[0])
print("Last letter:", s[-1])
print(s + " is " + str(len(s)) + " letters long")
print((s + " ") * 2)

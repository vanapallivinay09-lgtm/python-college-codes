# Day - Nested Conditional Statements

# Example 1: Simple nested
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")
    has_id = input("Do you have ID? yes/no: ")
    if has_id == "yes":
        print("You can vote")
    else:
        print("Get ID first")
else:
    print("Not adult")

# Example 2: Grade + Attendance (real college example)
print("\n--- Final Result ---")
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance %: "))

if marks >= 40:
    print("Pass in marks")
    if attendance >= 75:
        print("Pass overall - Promoted!")
    else:
        print("Fail due to low attendance")
else:
    print("Fail in marks")
    if attendance < 75:
        print("Also low attendance")

# Example 3: Login with 2 levels (like AWS Route53 + S3)
print("\n--- 3 Level Nested ---")
username = input("\nEnter username: ")
if username == "vinay":
    password = input("Enter password: ")
    if password == "1234":
        otp = input("Enter OTP 9999: ")
        if otp == "9999":
            print("Login Success - All 3 levels passed!")
        else:
            print("OTP wrong")
    else:
        print("Password wrong")
else:
    print("Username wrong")

# Example 4: Number check - positive/negative + even/odd
num = int(input("\nEnter number: "))
if num != 0:
    if num > 0:
        print("Positive", end=" - ")
    else:
        print("Negative", end=" - ")
    
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Zero")

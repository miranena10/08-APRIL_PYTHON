# Taking input from user
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))

# Nested if to check eligibility
if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood")
    else:
        print("You are not eligible (weight must be at least 50 kg)")
else:
    print("You are not eligible (age must be at least 18)")
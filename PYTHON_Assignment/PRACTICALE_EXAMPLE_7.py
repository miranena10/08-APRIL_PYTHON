# Taking percentage input
percentage = float(input("Enter your percentage: "))

# Grade calculation using if-elif-else ladder
if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F (Fail)")
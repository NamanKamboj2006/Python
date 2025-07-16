# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks = int(input("Enter Your Marks: "))

if marks >= 90 and marks <= 100:
    print(f"You got Ex Grade with a score of {marks}")
elif marks >= 80 and marks < 90:
    print(f"You got A Grade with a score of {marks}")
elif marks >= 70 and marks < 80:
    print(f"You got B Grade with a score of {marks}")
elif marks >= 60 and marks < 70:
    print(f"You got C Grade with a score of {marks}")
elif marks >= 50 and marks < 60:
    print(f"You got D Grade with a score of {marks}")
elif marks >= 0 and marks < 50:
    print(f"You got F Grade with a score of {marks}")
else:
    print("Invalid Marks! Please enter a value between 0 and 100.")

"""
if 90 <= marks <= 100:
    print(f"You got Ex Grade with a score of {marks}")
elif 80 <= marks < 90:
    print(f"You got A Grade with a score of {marks}")
elif 70 <= marks < 80:
    print(f"You got B Grade with a score of {marks}")
elif 60 <= marks < 70:
    print(f"You got C Grade with a score of {marks}")
elif 50 <= marks < 60:
    print(f"You got D Grade with a score of {marks}")
elif 0 <= marks < 50:
    print(f"You got F Grade with a score of {marks}")
else:
    print("Invalid Marks! Please enter a value between 0 and 100.")"""
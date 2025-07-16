# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# Write a program to find out whether a student has passed or failed
# Conditions:
# - At least 33% in each subject
# - At least 40% overall average

sub1 = float(input("Enter 1st Subject Marks: "))
sub2 = float(input("Enter 2nd Subject Marks: "))
sub3 = float(input("Enter 3rd Subject Marks: "))

average = (sub1 + sub2 + sub3) / 3

if sub1 < 33 or sub2 < 33 or sub3 < 33:
    print("Fail: You scored less than 33 in one or more subjects.")
elif average < 40: 
    print(f"Fail: Your average is {average:.2f}%, which is below 40%.")
else:
    print(f"Pass: Congratulations! You passed with {average:.2f}% average.")

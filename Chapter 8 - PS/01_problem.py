# Write a program using functions to find greatest of three numbers.

def greatest(x,y,z):
    greatest = max(x,y,z)
    return greatest

x = int(input("Enter 1st Num: "))
y = int(input("Enter 2nd Num: "))
z = int(input("Enter 3rd Num: "))

print(f"Greatest Number: {greatest(x,y,z)}")
